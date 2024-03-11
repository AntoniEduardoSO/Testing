import { setores } from "./setores.js";
import biuldSectorCard from "./biuldSectorCard.js";

export default function selectSection() {
  const sectors = document.querySelectorAll('[data-type="sector"]');

  sectors.forEach((sector) => {
    sector.addEventListener("click", handleSector);
  });

  function handleSector(element) {
    const sector = element.currentTarget;
    sectors.forEach((sector) => {
      sector.classList.remove("active");
    });
    sector.classList.add("active");
    const idSector = sector.dataset.id;
    setores.forEach((setor) => {
      if (setor.id === idSector) {
        biuldSectorCard(setor);
      }
    });
  }
}
