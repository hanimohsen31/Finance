export function Sorting(Data) {
  let mainArr = [];
  let tempArr = [];
  let initialObj = {};
  Data.map((elm, indx) => {
    // first itiration
    if (indx == 0) {
      initialObj = elm;
    }
    // conditon
    if (elm.Date.slice(0, 10) == initialObj.Date.slice(0, 10)) {
      tempArr.push(elm);
      // last itiration
      if (indx === Data.length - 1) {
        let x = tempArr.sort((a, b) => a.G10gm - b.G10gm);
        mainArr.push(x[0], x[x.length - 1]);
      }
    } else {
      let x = tempArr.sort((a, b) => a.G10gm - b.G10gm);
      mainArr.push(x[0], x[x.length - 1]);
      // reset
      tempArr = [];
      initialObj = Data[indx + 1];
      // push
      tempArr.push(elm);
    }
  });
  // console.log(mainArr)
  return mainArr
}