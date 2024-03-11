export default function warning() {
  const warning = document.querySelector('[data-type="warning"]');
  const close = document.querySelector('[data-warning="close"]');

  warning.addEventListener("click", closeWarning);
  close.addEventListener("click", closeWarning);

  function closeWarning(event) {
    if (event.target == event.currentTarget) {
      warning.classList.add("active");
    }
  }
}
