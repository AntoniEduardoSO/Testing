import JSONsector from "../json/sectors.js";
const sectors = JSON.parse(JSONsector);

const modalContainer = document.querySelector('[ data-modal="container"]');
const modal = document.querySelector('[data-modal="modal"]');

const closeModalButton = document.querySelectorAll('[data-modal="close"]');

function closeModal1(event) {
  if (event.target == this) {
    modalContainer.classList.remove("active");
  }
}

function closeModal2() {
  modalContainer.classList.remove("active");
}

export default function handleModal(event) {
  const sectorFinded = sectors.find(
    (sector) => +event.currentTarget.querySelector(".id").innerText == sector.id
  );

  modal.querySelector("[data-modal='tagname']").innerText =
    sectorFinded.tagname;
  modal.querySelector("[data-modal='name']").innerText = sectorFinded.name;
  modal.querySelector("[data-modal='biuld']").innerText = sectorFinded.biuld;
  modal.querySelector("[data-modal='contact']").innerText =
    sectorFinded.contact;
  modal.querySelector("[data-modal='supervisor']").innerText =
    sectorFinded.supervisor;
  modal.querySelector("[data-modal='location']").value = sectorFinded.location;
  modal
    .querySelector("[data-modal='change']")
    .setAttribute("data-id", sectorFinded.id);
    modal
    .querySelector("[data-modal='change']")
    .setAttribute("href", `http://192.168.48.21:8000/dashboard/semap/modificarsetor/${sectorFinded.id}`);

  modalContainer.classList.add("active");
}

if (modalContainer) {
  modalContainer.addEventListener("click", closeModal1);
  closeModalButton.forEach((item) => {
    item.addEventListener("click", closeModal2);
  });
}