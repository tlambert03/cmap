var chart_canvases = document.getElementsByClassName("linearity-chart");
for (var i = 0; i < chart_canvases.length; i++) {
  makeLinearityChart(chart_canvases[i]);
}

var chart_canvases = document.getElementsByClassName("rgb-chart");
for (var i = 0; i < chart_canvases.length; i++) {
  makeRGBChart(chart_canvases[i]);
}

var chart_canvases = document.getElementsByClassName("hsl-chart");
for (var i = 0; i < chart_canvases.length; i++) {
  makeHSLChart(chart_canvases[i]);
}

// FIXME: we're fetching data three times here.

//////////

GLOBAL_OPTIONS = {
  interaction: { mode: "index", intersect: false },
  plugins: { legend: { display: false } },
};

async function makeLinearityChart(canvas) {
  var cmap_name = canvas.getAttribute("data-cmap-name");
  const response = await fetch(`/cmap/data/${cmap_name}.json`);
  const cmap_data = await response.json();

  var lightness_data = [];
  var deltas = [];
  var colors = [];
  for (i = 0; i < cmap_data.length; i++) {
    lightness_data.push({ x: cmap_data[i].x, y: cmap_data[i].J });
    deltas.push({ x: cmap_data[i].x, y: cmap_data[i].lightness_derivs });
    colors.push(cmap_data[i].color);
  }

  new Chart(canvas, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: "lightness",
          backgroundColor: colors,
          data: lightness_data,
          pointRadius: 12,
          borderWidth: 0,
        },
        {
          label: "perceptual lightness derivatives",
          data: deltas,
          showLine: true,
          radius: 0,
          borderColor: "#00000044",
          borderWidth: 3,
          yAxisID: "y2",
        },
      ],
    },
    options: {
      ...GLOBAL_OPTIONS,
      scales: {
        y: { max: 100, min: 0, title: { text: "Lightness L*", display: true } },
        y2: {
          max: 500,
          min: -500,
          title: { text: "Perceptual Lightness Deltas", display: true },
          position: "right",
        },
      },
    },
  });
}

async function makeRGBChart(canvas) {
  var cmap_name = canvas.getAttribute("data-cmap-name");
  const response = await fetch(`/cmap/data/${cmap_name}.json`);
  const cmap_data = await response.json();

  var rdata = [];
  var gdata = [];
  var bdata = [];
  for (i = 0; i < cmap_data.length; i++) {
    rdata.push({ x: cmap_data[i].x, y: cmap_data[i].R });
    gdata.push({ x: cmap_data[i].x, y: cmap_data[i].G });
    bdata.push({ x: cmap_data[i].x, y: cmap_data[i].B });
  }

  new Chart(canvas, {
    type: "scatter",
    data: {
      datasets: [
        { label: "red", showLine: true, borderColor: "#BB0000BB", data: rdata },
        {
          label: "green",
          showLine: true,
          borderColor: "#00CC00BB",
          data: gdata,
        },
        {
          label: "blue",
          showLine: true,
          borderColor: "#0000FFBB",
          data: bdata,
        },
      ],
    },
    options: {
      ...GLOBAL_OPTIONS,
      scales: {
        y: {
          max: 1,
          min: 0,
          title: { text: "Component Value", display: true },
        },
      },
      elements: {
        line: { borderWidth: 4 },
        point: { radius: 0 },
      },
    },
  });
}

async function makeHSLChart(canvas) {
  var cmap_name = canvas.getAttribute("data-cmap-name");
  const response = await fetch(`/cmap/data/${cmap_name}.json`);
  const cmap_data = await response.json();

  var hue = [];
  var saturation = [];
  var chroma = [];
  for (i = 0; i < cmap_data.length; i++) {
    hue.push({ x: cmap_data[i].x, y: (cmap_data[i].hue * 100) / 360 });
    saturation.push({ x: cmap_data[i].x, y: cmap_data[i].saturation });
    chroma.push({ x: cmap_data[i].x, y: cmap_data[i].chroma });
  }

  new Chart(canvas, {
    type: "scatter",
    data: {
      datasets: [
        { label: "hue", showLine: true, data: hue },
        { label: "saturation", showLine: true, data: saturation },
        { label: "chroma", showLine: true, data: chroma },
      ],
    },
    options: {
      ...GLOBAL_OPTIONS,
      plugins: { legend: { display: true } },
      scales: {},
      elements: {
        line: { borderWidth: 4 },
        point: { radius: 0 },
      },
    },
  });
}
