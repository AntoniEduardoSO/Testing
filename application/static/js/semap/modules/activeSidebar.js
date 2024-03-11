import initMapSector from "./idSector.js";

export default function activeSidebar(sector) {
  if (sector) {
    if (mapContainer.dataset.status === "extended") {
      feedSidebar(sector);
      changeSidebar("minimized");
      mapContainer.dataset.status = "minimized";
    } else {
      feedSidebar(sector);
    }
  }
}

const sidebar = document.querySelector('[data-type="sidebar"]');
const closeSidebar = document.querySelector('[data-sidebar="close-sidebar"]');
const mapContainer = document.querySelector('[data-type="map-container"]');
const sidebarContainer = document.querySelector(
  '[data-type="sidebar-container"]'
);

closeSidebar.addEventListener("click", function () {
  changeSidebar("extended");
});

function changeSidebar(status) {
  if (status === "minimized") {
    sidebarContainer.classList.toggle("active");
    sidebar.classList.toggle("active");
  } else {
    sidebarContainer.classList.toggle("active");
    sidebar.classList.toggle("active");
    initMapSector(1);
    mapContainer.dataset.status = "extended";
  }
}

function feedSidebar(sector) {
  initMapSector(sector.id);
  const single = sidebar.querySelector('[data-sidebar="single"]');
  const title = sidebar.querySelector('[data-sidebar="title"]');
  const biuld = sidebar.querySelector('[data-sidebar="biuld"]');
  const location = sidebar.querySelector('[data-sidebar="location"]');
  single.innerText = sector.single;
  title.innerText = sector.name;
  biuld.innerText = sector.biuld;
  location.innerText = sector.location;
}
