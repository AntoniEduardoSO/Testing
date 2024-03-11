const mapNumbers = () => {
    const fontSettings = {
      fill: "#B2CDEC",
      fontWeight: "bold",
      length: 2,
    };
  
    const bgFontSettings = {
      width: "28",
      height: "32",
      fill: "#254594",
      stroke: "#5C76B6",
      strokeWidth: "1",
      rx: "4",
      ry: "4",
      length: 7,
    };
  
    const areasFont = document.querySelectorAll(".font-map");
    const bgAreaFont = document.querySelectorAll(".bg-font-map");
    const svgs = document.querySelectorAll(".area");
  
    bgAreaFont.forEach((bg) => configAttributes(bg));
    areasFont.forEach((bg) => configAttributes(bg));
    svgs.forEach((svg) => addConfig(svg));
  
    function configAttributes(mapElement) {
      let arraySettings;
  
      if (mapElement.tagName === "rect") {
        arraySettings = Object.entries(bgFontSettings);
      } else {
        arraySettings = Object.entries(fontSettings);
      }
  
      arraySettings.forEach((setting) => {
        mapElement.setAttribute(setting[0], setting[1]);
      });
    }
  
    function addConfig(svg) {
      svg.setAttribute("max-width", "100%");
      svg.setAttribute("height", "100%");
    }
  };
  
  const resizeChart = () => {
    const chartContainer = document.querySelector(".chart-container");
    const chart = chartContainer.querySelector("img");
  
    let newDimensions = [chartContainer.offsetWidth, chartContainer.offsetHeight];
    newDimensions.forEach((dimension, index) => {
      let newDimension = dimension + 8;
      if (index === 0) {
        chart.style.width = newDimension + "px";
      } else {
        chart.style.height = newDimension + "px";
      }
    });
  };
  
  // Adicionando a função como um ouvinte para o evento de redimensionamento da janela
  window.addEventListener("resize", resizeChart);
  window.addEventListener("resize", testando);
  
  function testando() {
    let newElement = document.createElement("li");
    const teste = document.querySelector(".infrastructor .card-info");
    const miseria = document.querySelector(".transporte-li");
    const small = window.matchMedia("(max-width: 1537px)");
  
    if (!!small.matches) {
      console.log("menor");
    } else {
      teste.removeChild(teste.querySelector(".transporte-li"));
    }
  }
  
  mapNumbers();