import clickOutside from "./outsideclick.js";
export default function menumobile() {
  const button = document.querySelector("[data-menu]");
  const events = ["click", "touchstart"];

  events.forEach((event) => {
    button.addEventListener(event, handleMenu);
  });

  function handleMenu(event) {
    const menu = document.querySelector(".nav-list");
    menu.classList.add("active");
    clickOutside(menu, events, () => {
      menu.classList.remove("active");
    });
  }
}
