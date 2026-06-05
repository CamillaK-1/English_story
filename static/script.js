document.addEventListener("DOMContentLoaded", () => {

    const buttons = document.querySelectorAll(".choice-btn");

    buttons.forEach(button => {

        button.addEventListener("mouseenter", () => {

            button.style.transition = "0.3s ease";
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", (event) => {

            event.preventDefault();

            const page = document.querySelector(".flipbook .page");
            if (!page) {
                form.submit();
                return;
            }

            // build a temporary flipbook overlay and animate with turn.js
            const rect = page.getBoundingClientRect();

            const overlay = document.createElement('div');
            overlay.className = 'flipbook-overlay';
            document.body.appendChild(overlay);

            // create flipbook container
            const flipbook = document.createElement('div');
            flipbook.className = 'flipbook';
            flipbook.style.width = Math.round(rect.width) + 'px';
            flipbook.style.height = Math.round(rect.height) + 'px';
            overlay.appendChild(flipbook);

            // create two pages: current (clone) and a blank/back page
            const p1 = document.createElement('div');
            p1.className = 'book-page';
            // clone only the visible content to reduce DOM weight
            const sourceContent = page.querySelector('.page-content');
            if (sourceContent) {
                p1.appendChild(sourceContent.cloneNode(true));
            } else {
                p1.innerHTML = page.innerHTML;
            }

            const p2 = document.createElement('div');
            p2.className = 'book-page';
            // populate second page from form's next page data
            const nextPageData = form.querySelector('.next-page-data');
            if (nextPageData) {
                const pageContent = nextPageData.querySelector('.page-content');
                if (pageContent) {
                    p2.appendChild(pageContent.cloneNode(true));
                } else {
                    p2.appendChild(nextPageData.cloneNode(true));
                }
            } else {
                p2.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100%;font-size:20px;color:var(--brown-dark);">Turning…</div>';
            }

            // ensure pages have explicit paper background to avoid white flashes
            const paperBg = 'linear-gradient(180deg, var(--paper), var(--paper-dark))';
            p1.style.background = paperBg;
            p2.style.background = paperBg;

            flipbook.appendChild(p1);
            flipbook.appendChild(p2);

            // position overlay to center over current page
            overlay.style.position = 'fixed';
            overlay.style.left = '0';
            overlay.style.top = '0';
            overlay.style.width = '100vw';
            overlay.style.height = '100vh';
            overlay.style.display = 'grid';
            overlay.style.placeItems = 'center';
            overlay.style.zIndex = 99999;
            overlay.style.overflow = 'hidden';

            // Ensure turn.js is loaded
            if (typeof jQuery === 'undefined' || !jQuery.fn.turn) {
                console.warn('turn.js not loaded, submitting directly');
                overlay.remove();
                form.submit();
                return;
            }

            let formSubmitted = false;

            try {
                // Initialize turn.js
                $(flipbook).turn({
                    width: rect.width,
                    height: rect.height,
                    autoCenter: true,
                    display: 'single',
                    duration: 700,
                    gradients: true,
                    acceleration: true
                });

                // Handler for when page turn completes
                const handleTurned = (e, pageNum) => {
                    if (!formSubmitted && pageNum === 2) {
                        formSubmitted = true;
                        try {
                            $(flipbook).off('turned', handleTurned);
                            $(flipbook).turn('destroy');
                        } catch(e) {}
                        overlay.remove();
                        form.submit();
                    }
                };

                // Bind the turned event
                $(flipbook).on('turned', handleTurned);

                // Request animation frame to ensure layout is complete before turning
                requestAnimationFrame(() => {
                    $(flipbook).turn('page', 2);
                });

                // Safety timeout in case turned event never fires
                setTimeout(() => {
                    if (!formSubmitted) {
                        formSubmitted = true;
                        try {
                            $(flipbook).off('turned', handleTurned);
                            $(flipbook).turn('destroy');
                        } catch(e) {}
                        overlay.remove();
                        form.submit();
                    }
                }, 1200);

            } catch (err) {
                console.error('turn.js error:', err);
                overlay.remove();
                form.submit();
            }

        });

    });

});