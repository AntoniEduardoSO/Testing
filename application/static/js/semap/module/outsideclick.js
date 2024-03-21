export default function clickoutSide(element, events, callback) {
  const html = document.documentElement;

  if (!element.hasAttribute("outside")) {
    setTimeout(() => {
      html.addEventListener("click", handleOutsideClick);
    });
    element.setAttribute("outside", "");
  } else {
    element.removeAttribute("outside");
    events.forEach((userEvent) => {
      html.removeEventListener(userEvent, handleOutsideClick);
    });
    callback();
  }

  function handleOutsideClick(event) {
    if (!element.contains(event.target)) {
      element.removeAttribute("outside");
      events.forEach((userEvent) => {
        html.removeEventListener(userEvent, handleOutsideClick);
      });
      callback();
    }
  }
}
