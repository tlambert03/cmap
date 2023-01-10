var chart_canvases = document.getElementsByClassName("linearity-chart");
for (var i = 0; i < chart_canvases.length; i++) {
  makeLinearityChart(chart_canvases[i]);
}

var chart_canvases = document.getElementsByClassName("rgb-chart");
for (var i = 0; i < chart_canvases.length; i++) {
  makeRGBChart(chart_canvases[i]);
}

//////////

async function makeLinearityChart(canvas) {
  var cmap_name = canvas.getAttribute("data-cmap-name");
  const response = await fetch(`/cmap/assets/_data/${cmap_name}.json`);
  const cmap_data = await response.json();

  var lightness_data = [];
  var colors = [];
  for (i = 0; i < cmap_data.length; i++) {
    lightness_data.push({ x: cmap_data[i].x, y: cmap_data[i].J });
    colors.push(cmap_data[i].color);
  }

  new Chart(canvas, {
    type: "scatter",
    data: {
      datasets: [
        {
          backgroundColor: colors,
          data: lightness_data,
          pointRadius: 12,
          borderWidth: 0,
        },
      ],
    },
    options: {
      animation: { duration: 400 },
      scales: {
        y: { max: 100, min: 0, title: { text: "Lightness L*", display: true } },
      },
      plugins: { legend: { display: false } },
    },
  });
}

async function makeRGBChart(canvas) {
  var cmap_name = canvas.getAttribute("data-cmap-name");
  const response = await fetch(`/cmap/assets/_data/${cmap_name}.json`);
  const cmap_data = await response.json();

  var rdata = [];
  var gdata = [];
  var bdata = [];
  var labels = [];
  for (i = 0; i < cmap_data.length; i++) {
    labels.push(cmap_data[i].x);
    rdata.push(cmap_data[i].R);
    gdata.push(cmap_data[i].G);
    bdata.push(cmap_data[i].B);
  }

  new Chart(canvas, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        { label: "red", borderColor: "#FF0000BB", data: rdata },
        { label: "green", borderColor: "#00AA00BB", data: gdata },
        { label: "blue", borderColor: "#0000FFBB", data: bdata },
      ],
    },
    options: {
      animation: { duration: 400 },
      scales: {
        y: {
          max: 1,
          min: 0,
          title: { text: "Component Value", display: true },
        },
        x: {
          ticks: {
            callback: function (val, index) {
              return index % 10 === 0 ? this.getLabelForValue(val) : "";
            },
            maxTicksLimit: 11,
            autoSkip: true,
            maxRotation: 0,
          },
        },
      },
      plugins: { legend: { display: false } },
      elements: { point: { radius: 0 }, line: { borderWidth: 4 } },
    },
  });
}
