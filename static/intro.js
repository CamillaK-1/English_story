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