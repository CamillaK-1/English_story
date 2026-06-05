document.addEventListener("DOMContentLoaded", () => {

    // Button hover enhancement
    const buttons = document.querySelectorAll(".choice-btn");

    buttons.forEach(button => {
        button.addEventListener("mouseenter", () => {
            button.style.transition = "0.3s ease";
        });
    });

    // Story form handling
    const forms = document.querySelectorAll(".story-form");

    forms.forEach(form => {

        form.addEventListener("submit", (event) => {

            event.preventDefault();

            const page = document.querySelector(".flipbook .page");

            if (!page) {
                form.submit();
                return;
            }

            const wrapper = document.querySelector(".book-wrapper");

            // Hide original book immediately
            if (wrapper) {
                wrapper.style.visibility = "hidden";
            }

            const rect = page.getBoundingClientRect();

            // Create overlay
            const overlay = document.createElement("div");
            overlay.className = "flipbook-overlay";

            overlay.style.position = "fixed";
            overlay.style.left = "0";
            overlay.style.top = "0";
            overlay.style.width = "100vw";
            overlay.style.height = "100vh";
            overlay.style.display = "grid";
            overlay.style.placeItems = "center";
            overlay.style.zIndex = "99999";
            overlay.style.overflow = "hidden";

            document.body.appendChild(overlay);

            // Create flipbook
            const flipbook = document.createElement("div");
            flipbook.className = "flipbook";

            flipbook.style.width = Math.round(rect.width) + "px";
            flipbook.style.height = Math.round(rect.height) + "px";

            overlay.appendChild(flipbook);

            // PAGE 1 = current chapter
            const p1 = document.createElement("div");
            p1.className = "book-page";

            const sourceContent =
                page.querySelector(".page-content");

            if (sourceContent) {
                p1.appendChild(
                    sourceContent.cloneNode(true)
                );
            }

            // PAGE 2 = next chapter
            const p2 = document.createElement("div");
            p2.className = "book-page";

            const template =
                document.querySelector("#next-page-template");

            if (template) {
                p2.innerHTML = template.innerHTML;
            }

            const paperBg =
                "linear-gradient(180deg, var(--paper), var(--paper-dark))";

            p1.style.background = paperBg;
            p2.style.background = paperBg;

            flipbook.appendChild(p1);
            flipbook.appendChild(p2);

            // turn.js fallback
            if (
                typeof jQuery === "undefined" ||
                !jQuery.fn.turn
            ) {

                overlay.remove();

                if (wrapper) {
                    wrapper.style.visibility = "visible";
                }

                form.submit();
                return;
            }

            let submitted = false;

            const cleanup = () => {

                try {
                    $(flipbook).turn("destroy");
                } catch (e) {}

            };

            try {

                $(flipbook).turn({
                    width: rect.width,
                    height: rect.height,
                    display: "single",
                    autoCenter: true,
                    duration: 650,
                    gradients: true,
                    acceleration: true
                });

                const handleTurned = (e, pageNum) => {

                    if (pageNum === 2 && !submitted) {

                        submitted = true;

                        // submit immediately
                        form.submit();
                    }
                };

                $(flipbook).on(
                    "turned",
                    handleTurned
                );

                requestAnimationFrame(() => {

                    $(flipbook).turn(
                        "page",
                        2
                    );
                });

                // emergency fallback
                setTimeout(() => {

                    if (!submitted) {

                        submitted = true;

                        cleanup();

                        form.submit();
                    }

                }, 700);

            } catch (err) {

                console.error(err);

                cleanup();

                if (wrapper) {
                    wrapper.style.visibility =
                        "visible";
                }

                form.submit();
            }

        });

    });

});