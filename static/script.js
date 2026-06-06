document.addEventListener("DOMContentLoaded", () => {

    // Button hover enhancement
    const buttons = document.querySelectorAll(".choice-btn");

    buttons.forEach(button => {
        button.addEventListener("mouseenter", () => {
            button.style.transition = "0.3s ease";
        });
    });

    // Story form handling – no flash, animation intact
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
            const rect = page.getBoundingClientRect();

            // Create overlay – start fully visible but transparent? No, we'll build it in place
            const overlay = document.createElement("div");
            overlay.className = "flipbook-overlay";

            overlay.style.position = "fixed";
            overlay.style.left = rect.left + "px";
            overlay.style.top = rect.top + "px";
            overlay.style.width = rect.width + "px";
            overlay.style.height = rect.height + "px";
            overlay.style.zIndex = "99999";
            overlay.style.overflow = "hidden";
            // Initially make it take no space but be ready
            overlay.style.opacity = "0";
            overlay.style.visibility = "hidden";

            document.body.appendChild(overlay);

            // Build flipbook with exact dimensions
            const flipbook = document.createElement("div");
            flipbook.className = "flipbook";
            flipbook.style.width = "100%";
            flipbook.style.height = "100%";

            overlay.appendChild(flipbook);

            // PAGE 1 = clone of original page but with text/children hidden
            const p1 = document.createElement("div");
            p1.className = "book-page";

            const sourceContent = page.querySelector(".page-content");
            if (sourceContent) {
                const clone = sourceContent.cloneNode(true);
                // Hide all content (text, images, etc.) but keep background
                clone.style.opacity = "0";
                clone.style.visibility = "hidden";
                p1.appendChild(clone);
            }
            // Copy computed background from original page
            const originalBg = window.getComputedStyle(page).background;
            p1.style.background = originalBg;

            // PAGE 2 = next chapter with placeholder during animation
            const p2 = document.createElement("div");
            p2.className = "book-page";

            const template = document.querySelector("#next-page-template");
            let contentClone = null;
            if (template) {
                contentClone = template.cloneNode(true);
                // Remove the display:none style from template
                contentClone.style.display = "";
                // Initially hide the content
                contentClone.style.opacity = "0";
                contentClone.style.visibility = "hidden";
                p2.appendChild(contentClone);
            }
            
            // Set background to match the expected page background
            p2.style.background = originalBg;

            flipbook.appendChild(p1);
            flipbook.appendChild(p2);

            // turn.js check
            if (typeof jQuery === "undefined" || !jQuery.fn.turn) {
                overlay.remove();
                if (wrapper) wrapper.style.visibility = "visible";
                form.submit();
                return;
            }

            let submitted = false;
            const cleanup = () => {
                try { $(flipbook).turn("destroy"); } catch(e) {}
            };

            try {
                // Initialize turn.js, start on page 1 (which looks blank but matches background)
                $(flipbook).turn({
                    width: rect.width,
                    height: rect.height,
                    display: "single",
                    autoCenter: true,
                    duration: 650,
                    gradients: true,
                    acceleration: true,
                    page: 1
                });

                // CRITICAL: Position overlay exactly over original, then make it visible
                // and hide original in the same paint frame – no gap
                requestAnimationFrame(() => {
                    // Update position in case of scroll
                    const newRect = page.getBoundingClientRect();
                    overlay.style.left = newRect.left + "px";
                    overlay.style.top = newRect.top + "px";
                    
                    requestAnimationFrame(() => {
                        overlay.style.visibility = "visible";
                        overlay.style.opacity = "1";
                        if (wrapper) wrapper.style.visibility = "hidden";
                        
                        // Start the flip animation immediately
                        $(flipbook).turn("page", 2);
                    });
                });

                const handleTurned = (e, pageNum) => {
                    if (pageNum === 2 && !submitted) {
                        submitted = true;
                        
                        // After flip completes, fade in the content quickly
                        if (contentClone) {
                            contentClone.style.visibility = "visible";
                            contentClone.style.transition = "opacity 0.4s ease-in";
                            
                            // Trigger reflow to ensure the visibility change takes effect
                            void contentClone.offsetHeight;
                            
                            contentClone.style.opacity = "1";
                        }
                        
                        // Submit form after content fade is complete
                        setTimeout(() => form.submit(), 600);
                    }
                };

                $(flipbook).on("turned", handleTurned);

                // Safety timeout
                setTimeout(() => {
                    if (!submitted) {
                        submitted = true;
                        cleanup();
                        form.submit();
                    }
                }, 2500);

            } catch (err) {
                console.error(err);
                cleanup();
                if (wrapper) wrapper.style.visibility = "visible";
                form.submit();
            }
        });
    });
});


