export default function searchJSON() {}

import initClean from "./clean.js";
import initGetSector from "./get-sector.js";

const form = document.forms.sectors;

console.log(form);

if (form) {
  const searchInput = document.forms.sectors.search;
  const formButton = document.forms.sectors.querySelector("button");
  const biuldSelect = document.querySelector("#biuld");

  form.addEventListener("submit", dontSubmit);
  formButton.addEventListener("click", search);

  function dontSubmit(e) {
    e.preventDefault();
  }

  function search(e) {
    const input = initClean(searchInput.value);
    const option = initClean(biuldSelect.value);

    console.log(input);

    initGetSector.show(initGetSector.search(input, option), "some");
  }
}
