// ============================================================
// NAV.JS — Lógica del sidebar y navegación entre secciones
// ============================================================

// Abre o cierra el sidebar
function toggleSidebar() {
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('overlay');

  sidebar.classList.toggle('abierto');
  overlay.classList.toggle('visible');
}

// Cierra el sidebar siempre (sin toggle)
function cerrarSidebar() {
  var sidebar = document.getElementById('sidebar');
  var overlay = document.getElementById('overlay');

  sidebar.classList.remove('abierto');
  overlay.classList.remove('visible');
}

// Muestra la sección que se pidió y oculta las demás
function mostrarSeccion(id) {
  // 1. Quita la clase "activa" de todas las secciones
  var secciones = document.querySelectorAll('.seccion');
  secciones.forEach(function(seccion) {
    seccion.classList.remove('activa');
  });

  // 2. Le pone "activa" solo a la sección pedida
  var seccionElegida = document.getElementById(id);
  if (seccionElegida) {
    seccionElegida.classList.add('activa');
  }

  // 3. Cierra el sidebar con remove (no toggle)
  cerrarSidebar();

  // 4. Sube la página al inicio
  window.scrollTo(0, 0);
}