import {Sorting} from './sorting.js'

let url = "https://finance-456dd-default-rtdb.firebaseio.com";
let xValues = [];
let G1gm = [];
let Dollar = [];
let rows = [];


fetch(`${url}/Data.json`).then(async (response) => {
  let data = await response.json();
  // data = Sorting(data)
  data.map((elm, indx) => {
    if (elm !== null) {
      xValues.push(elm?.Date.slice(0,10) || elm?.Date || "xxxx-xx-xx");
      let G1gmvar = +(+elm?.["G10gm"] / 10).toFixed(3);
      G1gm.push(G1gmvar);
      // dollar
      Dollar.push(+elm?.Dollar);

      let row = `
      <tr class="row${indx}">
        <th scope="col" class="NO">${indx}</th>
        <th scope="col">${elm?.Date}</th>
        <th scope="col">${G1gmvar}</th>
        <th scope="col" class="xG5gm" >${(+elm?.["G5gm"]).toFixed(3)}</th>
        <th scope="col" class="xG10gm" >${(+elm?.["G10gm"]).toFixed(3)}</th>
        <th scope="col" class="xG20gm" >${(+elm?.["G20gm"]).toFixed(3)}</th>
        <th scope="col" class="xG31gm" >${(+elm?.["G31gm"]).toFixed(3)}</th>
        <th scope="col" class="xG50gm" >${(+elm?.["G50gm"]).toFixed(3)}</th>
        <th scope="col" class="xDollar">${elm?.Dollar}</th>
        </tr>
      `;
      rows.push(row);
    }
  });

  rows.reverse();
  rows
    .slice(0, 30)
    .map((elm) => (document.querySelector("#tableRows").innerHTML += elm));

  new Chart("G1gm", {
    type: "line",
    display: true,
    position: "right",
    data: {
      labels: xValues,
      datasets: [
        {
          lineTension: 0,
          data: G1gm,
          borderColor: "yellow",
          // backgroundColor: "rgba(0,0,255,1.0)",
          // borderColor: "rgba(0,0,255,0.1)",
          fill: false,
          label: "1GM-24",
        },
      ],
    },
    options: {
      legend: { display: false },
    },
  });

  new Chart("Dollar", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [
        {
          lineTension: 0,
          data: Dollar,
          borderColor: "crimson",
          fill: false,
          label: "10GM-24",
        },
      ],
    },
    options: {
      legend: { display: false },
    },
  });
});
