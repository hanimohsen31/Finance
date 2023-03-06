function toggle(elm, name) {
  let btn = document.querySelector(`#${elm}`);
  let thisBtn = document.querySelector(`.${name}`);
  if (thisBtn.innerText === `Hide ${name}`) {
    thisBtn.innerText = `Show ${name}`;
  } else {
    thisBtn.innerText = `Hide ${name}`;
  }
  btn.classList.toggle("d-none");
}

function toggleCharts(elm1, elm2) {
  let btn1 = document.querySelector(`#${elm1}`);
  let btn2 = document.querySelector(`#${elm2}`);
  if (!btn1.classList.contains("d-none") & !btn2.classList.contains("d-none")) {
    btn2.classList.toggle("d-none");
  } else {
    btn1.classList.toggle("d-none");
    btn2.classList.toggle("d-none");
  }
}

function Delete(indx) {
  let url = "https://finance-456dd-default-rtdb.firebaseio.com";
  fetch(`${url}/Data/${indx}.json`, { method: "DELETE" }).then(
    async (response) => {
      let data = await response.json();
      console.log(data);
      document.querySelector(`.row${indx}`).style.display = "none";
    }
  );
}