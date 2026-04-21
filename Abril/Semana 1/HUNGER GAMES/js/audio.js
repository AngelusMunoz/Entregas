// ESTO ES PARA EL AUDIO

function iniciarAudio() {
    const intro = document.getElementById("intro");
    const fondo = document.getElementById("fondo");

    fondo.volume = 0.20;

    intro.play();

    intro.onended = function() {
        fondo.play();
    };
}