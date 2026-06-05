document.addEventListener("DOMContentLoaded", () => {

    const book = document.getElementById("introBook");

    const camera = document.getElementById("cameraView");

    let animating = false;

    book.addEventListener("click", () => {

        if (animating) return;

        animating = true;

        // move camera toward center
        camera.classList.add("move-center");

        // straighten book
        setTimeout(() => {

            book.classList.add("straight");

        }, 200);

        // open cover
        setTimeout(() => {

            book.classList.add("open");

        }, 1000);

        // cinematic zoom
        setTimeout(() => {

            camera.classList.add("zoom-in");

        }, 1450);

        // transition
        setTimeout(() => {

            window.location.href = "/story";

        }, 2100);

    });

});

document.addEventListener('DOMContentLoaded', () => {
    const splash = document.getElementById('splashScreen');
    const mainIntro = document.getElementById('mainIntro');

    // Gentle crossfade
    setTimeout(() => {
        splash.style.opacity = '0';
        
        // Start fading in the main scene while splash is still fading out
        setTimeout(() => {
            mainIntro.style.opacity = '1';
        }, 400); // slight overlap for smoother blend

        // Remove splash completely after transition
        setTimeout(() => {
            splash.style.display = 'none';
        }, 2800);
    }, 1600); // Time the splash is fully visible before starting fade
});