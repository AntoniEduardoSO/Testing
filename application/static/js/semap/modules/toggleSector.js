export default function activeSector(id) {
  const sectors = document.querySelectorAll('[data-type="sector"]');

  sectors.forEach((sector) => {
    sector.classList.toggle("active");
  });

  document.querySelector(`[data-id="${id}]"`).classList.toggle("active");
}
