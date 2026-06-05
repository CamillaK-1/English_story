document.addEventListener("DOMContentLoaded", () => {

    // Button hover enhancement
    const buttons = document.querySelectorAll(".choice-btn");
    buttons.forEach(button => {
        button.addEventListener("mouseenter", () => {
            button.style.transition = "0.3s ease";
        });
    });

    // Helper: initialize turn.js on the real flipbook
    function initTurnOnFlipbook() {
        const flipbook = document.querySelector(".book-wrapper .flipbook");
        if (!flipbook || typeof jQuery === "undefined" || !jQuery.fn.turn) return;
        const width = flipbook.clientWidth;
        const height = flipbook.clientHeight;
        $(flipbook).turn({
            width: width,
            height: height,
            display: "single",
            autoCenter: true,
            duration: 650,
            gradients: true,
            acceleration: true
        });
    }

    // Handle each story form
    const forms = document.querySelectorAll(".story-form");
    forms.forEach(form => {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();

            // Get current page element
            const page = document.querySelector(".flipbook .page");
            if (!page) {
                form.submit();
                return;
            }

            const wrapper = document.querySelector(".book-wrapper");
            if (wrapper) wrapper.style.visibility = "hidden";

            const rect = page.getBoundingClientRect();

            // Create overlay for the flip animation
            const overlay = document.createElement("div");
            overlay.className = "flipbook-overlay";
            overlay.style.cssText = `
                position: fixed;
                left: 0;
                top: 0;
                width: 100vw;
                height: 100vh;
                display: grid;
                place-items: center;
                z-index: 99999;
                overflow: hidden;
                background: #cab7a2;
            `;
            document.body.appendChild(overlay);

            // Create temporary flipbook
            const flipbook = document.createElement("div");
            flipbook.className = "flipbook";
            flipbook.style.width = Math.round(rect.width) + "px";
            flipbook.style.height = Math.round(rect.height) + "px";
            overlay.appendChild(flipbook);

            // Page 1: clone current page content
            const p1 = document.createElement("div");
            p1.className = "book-page";
            const sourceContent = page.querySelector(".page-content");
            if (sourceContent) p1.appendChild(sourceContent.cloneNode(true));
            p1.style.background = "linear-gradient(180deg, var(--paper), var(--paper-dark))";

            // Page 2: from hidden template (next chapter preview)
            const p2 = document.createElement("div");
            p2.className = "book-page";
            const template = document.querySelector("#next-page-template");
            if (template) p2.innerHTML = template.innerHTML;
            p2.style.background = "linear-gradient(180deg, var(--paper), var(--paper-dark))";

            flipbook.appendChild(p1);
            flipbook.appendChild(p2);

            // Check if turn.js is available
            if (typeof jQuery === "undefined" || !jQuery.fn.turn) {
                overlay.remove();
                if (wrapper) wrapper.style.visibility = "visible";
                form.submit();
                return;
            }

            let submitted = false;
            let fallbackTimer = null;

            const cleanup = () => {
                if (fallbackTimer) clearTimeout(fallbackTimer);
                try { $(flipbook).turn("destroy"); } catch(e) {}
                overlay.remove();
                if (wrapper) wrapper.style.visibility = "visible";
            };

            try {
                // Initialize turn.js on the temporary flipbook
                $(flipbook).turn({
                    width: rect.width,
                    height: rect.height,
                    display: "single",
                    autoCenter: true,
                    duration: 650,
                    gradients: true,
                    acceleration: true
                });

                // When flip reaches page 2, submit via AJAX
                const handleTurned = async (e, pageNum) => {
                    if (pageNum === 2 && !submitted) {
                        submitted = true;
                        if (fallbackTimer) clearTimeout(fallbackTimer);

                        const choiceInput = form.querySelector("input[name='choice']");
                        const choiceValue = choiceInput ? choiceInput.value : "";

                        try {
                            const response = await fetch("/story", {
                                method: "POST",
                                headers: {
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "X-Requested-With": "XMLHttpRequest"
                                },
                                body: new URLSearchParams({ choice: choiceValue })
                            });

                            if (!response.ok) throw new Error("Network error");

                            const html = await response.text();

                            // Check if we got an ending page
                            if (html.includes("Final Ending") || response.url.includes("ending")) {
                                window.location.href = "/ending";
                                return;
                            }

                            // Parse new content
                            const parser = new DOMParser();
                            const doc = parser.parseFromString(html, "text/html");
                            const newFlipbookContent = doc.querySelector(".flipbook");
                            const newNextPageTemplate = doc.querySelector("#next-page-template");

                            if (newFlipbookContent && wrapper) {
                                const realFlipbook = wrapper.querySelector(".flipbook");
                                if (realFlipbook) {
                                    try { $(realFlipbook).turn("destroy"); } catch(e) {}
                                    realFlipbook.outerHTML = newFlipbookContent.outerHTML;
                                }
                                const realTemplate = document.querySelector("#next-page-template");
                                if (realTemplate && newNextPageTemplate) {
                                    realTemplate.innerHTML = newNextPageTemplate.innerHTML;
                                }
                                initTurnOnFlipbook();
                            } else {
                                throw new Error("No new content");
                            }
                        } catch (err) {
                            console.error(err);
                            window.location.href = "/story";
                            return;
                        } finally {
                            cleanup();
                        }
                    }
                };

                $(flipbook).on("turned", handleTurned);

                // Start the page flip animation
                requestAnimationFrame(() => {
                    $(flipbook).turn("page", 2);
                });

                // Emergency fallback in case turn.js fails
                fallbackTimer = setTimeout(() => {
                    if (!submitted) {
                        submitted = true;
                        cleanup();
                        form.submit();
                    }
                }, 2000);

            } catch (err) {
                console.error(err);
                cleanup();
                form.submit();
            }
        });
    });

    // Initialize turn.js on page load
    initTurnOnFlipbook();
});