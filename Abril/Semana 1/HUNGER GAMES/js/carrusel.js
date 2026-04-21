// ESTO ES PARA EL CARRUSEL QUE SE USARA EN GENERAL PARA LAS PELICULAS

function moverCarrusel(boton, direccion) {
    const container = boton.closest(".carrusel-container");
    const carrusel = container.querySelector(".carrusel-peliculas");
    const puntos = container.querySelectorAll(".punto");

    const items = carrusel.children;
    let index = parseInt(carrusel.dataset.index);

    index += direccion;

    // límites (loop infinito)
    if (index < 0) index = items.length - 1;
    if (index >= items.length) index = 0;

    // guardar posición
    carrusel.dataset.index = index;

    // mover carrusel
    carrusel.style.transform = `translateX(-${index * 100}%)`;

    // actualizar puntos
    puntos.forEach((p, i) => {
        p.classList.toggle("activo", i === index);
    })
}
