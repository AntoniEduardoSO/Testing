import sectorsJSON from "../json/sectors.js";
import initClean from "./clean.js";
import initModal from "./modal.js";

const sectorListAPI = {
  sectors: JSON.parse(sectorsJSON),
  numberSector: document.querySelector("[data-sector='number']"),
  listSectors: document.getElementById("sector-list"),

  show(sectors) {
    this.listSectors.innerHTML = "";
    sectors.forEach((sector) => {
      this.listSectors.appendChild(this.build(sector));
    });
    this.numberSector.innerText =
      this.listSectors.getElementsByClassName("sector").length;
  },

  build(objectSector) {
    const sector = document.createElement("li");
    sector.classList.add("sector");
    sector.innerHTML = `<ul>
      <li class="id" data-id="${objectSector.id}">${objectSector.id}</li>
      <li class="name">${objectSector.name}</li>
      <li class="tag-name"><span class="tag">${objectSector.build}</span></li>
      <li class="location">${objectSector.location}</li>
      <li class="tag-name">${objectSector.tagname}</li>
    </ul>`;
    sector.addEventListener("click", initModal);
    return sector;
  },

  search(query, option) {
    const cleanedQuery = initClean(query);
    const cleanedOption = initClean(option);
    return this.sectors.filter((sector) => {
      const isQueryMatch =
        cleanedQuery === "" ||
        cleanedQuery === initClean(sector.name) ||
        cleanedQuery === initClean(sector.tagname) ||
        sector.othernames.some((name) => cleanedQuery === initClean(name));

      const isOptionMatch =
        option === "all" || cleanedOption === initClean(sector.build);
      return isQueryMatch && isOptionMatch;
    });
  },
};

if (document.forms.sectors) {
  window.onload =()=> {
    sectorListAPI.show(sectorListAPI.search("", "all"));
  };
}

export default sectorListAPI;
