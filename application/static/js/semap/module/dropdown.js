export default function dropdown() {}
import clickOutSide from "./outsideclick.js";

const dropdowns = document.querySelectorAll("[data-dropdown]");
const eventTypes = ["click", "touchstart"];

eventTypes.forEach((event) => {
  dropdowns.forEach((item) => {
    item.addEventListener(event, alterDropdown);
  });
});

function alterDropdown(event) {
  event.preventDefault();
  event.currentTarget.classList.add("active");
  clickOutSide(this, eventTypes, () => {
    this.classList.remove("active");
  });
}
