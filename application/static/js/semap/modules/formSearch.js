import initSibebar from "./activeSidebar.js";

export default function searchForm(setores) {
  const formInput = document.querySelector("[data-input]");
  let lastInput = "";
  formInput.addEventListener("keydown", findSector);

  function findSector(event) {
    const input = cleanString(formInput.value);
    if (
      (event.key === "Enter" || event.key === 13) &&
      input !== "" &&
      lastInput != input
    ) {
      if (input != lastInput) {
        let sectorFinded;
        setores.forEach((sector) => {
          const sectorKeys = sectorKeyNames(sector);
          sectorKeys.forEach((key) => {
            if (key === input) {
              sectorFinded = sector;
            }
          });
        });
        if (sectorFinded) {
          lastInput = input;
          return initSibebar(sectorFinded);
        } else {
          return alert("Setor não encontrado.");
        }
      } else {
        console.log(`${input} e diferente de ${lastInput}`);
      }
    }
  }

  function cleanString(input) {
    let newString = input.trim().toLowerCase();
    newString = newString
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[^a-zA-Z0-9 ]/g, "");
    return newString;
  }

  function sectorKeyNames(sector) {
    const sectorKeys = [];
    sectorKeys.push(sector.single);
    sectorKeys.push(cleanString(sector.name));
    sector.otherNames.forEach((name) => {
      sectorKeys.push(name);
    });
    return sectorKeys;
  }
}
