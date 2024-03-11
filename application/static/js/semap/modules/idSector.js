import initFeedSidebar from "./activeSidebar.js";
import { setores } from "./setores.js";
const sectors = Array.from(document.querySelectorAll("[data-sector]"));
const $ = console.log.bind(console);

export default function identifySector(sectorInput) {
  if (typeof sectorInput == "string") {
    const sectorFinded = sectors.find((sector) => {
      return sectorInput == sector.dataset.sector;
    });
    sectors.forEach((sector) => {
      sector.classList.remove("active");
    });
    sectorFinded.classList.add("active");
  } else if (sectorInput == 1) {
    sectors.forEach((sector) => {
      sector.classList.remove("active");
    });
  } else if (sectorInput == 2) {
    sectors.forEach((sector) => {
      sector.addEventListener("click", handleSector);
    });
  }
}

function handleSector(event) {
  sectors.forEach((sector) => {
    sector.classList.remove("active");
  });
  event.currentTarget.classList.add("active");
  const teste = findSector(event.currentTarget.dataset.sector);
  initFeedSidebar(teste);
}

function findSector(id) {
  return setores.find((setor) => {
    return setor.id === id;
  });
}
