export default function poligonos() {
  const ctfe1 = document.querySelector(".ctef-2");
  const ctfe2 = document.querySelector(".ctef-3");
  const ctfe3 = document.querySelector(".ctef-4");

  const setores = [ctfe1, ctfe2, ctfe3];

  setores.forEach((setor) => setor.addEventListener("mouseover", handleSetor));
  setores.forEach((setor) => setor.addEventListener("mouseenter", handleSetor));
  setores.forEach((setor) => setor.addEventListener("mouseleave", handleSetor));

  function handleSetor(event) {
    switch (event.type) {
      case "mouseover":
        setores.forEach((setor) => {
          setor.style.background = "#ff5915";
          setor.style.border = "1px solid #fff";
        });
      case "mouseenter":
        setores.forEach((setor) => {
          setor.style.background = "#ff5915";
          setor.style.border = "1px solid #fff";
        });
      case "mouseleave":
        setores.forEach((setor) => {
          setor.style.background = "#626262";
          setor.style.border = "1px solid #a8a8a";
        });
    }
  }
}
