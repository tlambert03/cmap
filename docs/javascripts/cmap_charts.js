initCharts();

async function initCharts() {
  var charts = document.getElementsByClassName("cmap-chart");
  if (charts.length == 0) {
    return;
  }

  var chartElems = {};
  // Make object mapping chart name to document element
  for (var i = 0; i < charts.length; i++) {
    var cmap_name = charts[i].getAttribute("data-cmap-name");
    if (cmap_name in chartElems) {
      chartElems[cmap_name].push(charts[i]);
    } else {
      chartElems[cmap_name] = [charts[i]];
    }
  }
  // Make all charts for each cmap name
  for (var cmap_name in chartElems) {
    // This is an ugly way to get the URL relative to root, but I couldn't
    // figure out how to get the root including "/en/latest" (or whatever
    // version is being viewed) in read the docs.  This at least will fail
    // locally as well if the cmap pages are moved
    const response = await fetch(`/data/${cmap_name}.json`);
    const cmap_data = await response.json();
    for (var i = 0; i < chartElems[cmap_name].length; i++) {
      var canv = chartElems[cmap_name][i];
      if (canv.classList.contains("rgb-chart")) {
        makeRGBChart(canv, cmap_data);
      } else if (canv.classList.contains("hsl-chart")) {
        makeHSLChart(canv, cmap_data);
      } else if (canv.classList.contains("linearity-chart")) {
        makeLinearityChart(canv, cmap_data);
      }
    }
  }
}

//////////

GLOBAL_OPTIONS = {
  interaction: { mode: "index", intersect: false },
  plugins: { legend: { display: false } },
  clip: false,
};

async function makeLinearityChart(canvas, cmap_data) {
  var lightness_data = [];
  var deltas = [];
  var a = [];
  var b = [];
  for (i = 0; i < cmap_data.x.length; i++) {
    lightness_data.push({ x: cmap_data.x[i], y: cmap_data.J[i] });
    deltas.push({ x: cmap_data.x[i], y: cmap_data.lightness_derivs[i] });
    // a.push({ x: cmap_data.x[i], y: cmap_data.a[i] })
    // b.push({ x: cmap_data.x[i], y: cmap_data.b[i] })
  }

  new Chart(canvas, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: "J",
          backgroundColor: cmap_data.color,
          data: lightness_data,
          pointRadius: 12,
          borderWidth: 0,
        },
        {
          label: "deltas",
          data: deltas,
          showLine: true,
          radius: 0,
          borderColor: "#AAAAAA66",
          borderWidth: 3,
          yAxisID: "y2",
        },
        // {
        //   label: "a",
        //   data: a,
        //   showLine: true,
        //   radius: 0,
        //   borderColor: "#AA222266",
        //   borderWidth: 2,
        //   yAxisID: "y3",
        // },
        // {
        //   label: "b",
        //   data: b,
        //   showLine: true,
        //   radius: 0,
        //   borderColor: "#2222AA66",
        //   borderWidth: 2,
        //   yAxisID: "y3",
        // },
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
        // y3: { max: 120, min: -120, display: false },
      },
    },
  });
}

async function makeRGBChart(canvas, cmap_data) {
  var rdata = [];
  var gdata = [];
  var bdata = [];
  for (i = 0; i < cmap_data.x.length; i++) {
    rdata.push({ x: cmap_data.x[i], y: cmap_data.R[i] });
    gdata.push({ x: cmap_data.x[i], y: cmap_data.G[i] });
    bdata.push({ x: cmap_data.x[i], y: cmap_data.B[i] });
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

async function makeHSLChart(canvas, cmap_data) {
  var datasets = [];
  var label_data, data, val;

  ["hue", "saturation", "chroma"].forEach((label) => {
    label_data = cmap_data[label];
    data = [];
    for (i = 0; i < cmap_data.x.length; i++) {
      val = label_data[i];
      data.push({
        x: cmap_data.x[i],
        y: label == "hue" ? (val * 10) / 36 : val,
      });
    }
    datasets.push({ label: label, showLine: true, data: data });
  });

  new Chart(canvas, {
    type: "scatter",
    data: { datasets: datasets },
    options: {
      ...GLOBAL_OPTIONS,
      plugins: { legend: { display: true, labels: { boxHeight: 1 } } },
      scales: {},
      elements: {
        line: { borderWidth: 4 },
        point: { radius: 0 },
      },
    },
  });
}
