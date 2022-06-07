const equ1x = document.getElementById("equ-1-x"),
  equ1y = document.getElementById("equ-1-y"),
  equ1Ans = document.getElementById("equ-1"),
  equ2x = document.getElementById("equ-2-x"),
  equ2y = document.getElementById("equ-2-y"),
  equ2Ans = document.getElementById("equ-2"),
  output = document.getElementById("result"),
  alertText = document.getElementById("alert"),
  form = document.getElementById("form");

document.addEventListener("DOMContentLoaded", equ1x.focus());
form.addEventListener("submit", calculateValues);

function resetInputFields() {
  equ1x.value = "";
  equ1y.value = "";
  equ1Ans.value = "";
  equ2x.value = "";
  equ2y.value = "";
  equ2Ans.value = "";
}

function calculateValues(e) {
  let x1 = Number(equ1x.value) || equ1x.value,
    y1 = Number(equ1y.value) || equ1y.value,
    z1 = Number(equ1Ans.value) || equ1Ans.value,
    x2 = Number(equ2x.value) || equ2x.value,
    y2 = Number(equ2y.value) || equ2y.value,
    z2 = Number(equ2Ans.value) || equ2Ans.value;
  // Display an alert if any of the input is invalid
  if (!(x1 && y1 && z1 && x2 && y2 && z2)) {
    alertText.classList.add("alert");
    alertText.textContent = "Invalid input";
  }
  // Removes the alert after 2 seconds
  setTimeout(() => {
    alertText.classList.remove("alert");
    alertText.textContent = "";
  }, 2000);

  const factorOne = x1,
    factorTwo = x2;
  //  Multiply equ2 through by either of the coefficient of equ1, (x1 in this case)
  (x2 = x2 * factorOne),
    (y2 = y2 * factorOne),
    (z2 = z2 * factorOne),
    //  Multiply equ1 by either of coefficent of equ2, (x2 in this case)
    (x1 = x1 * factorTwo),
    (y1 = y1 * factorTwo),
    (z1 = z1 * factorTwo);
  //  If x1 + x2 = 0 then add y1 + y2 (which gives y3) and z1 + z2 (which gives z3) ; else y1 - y2 and z1 - z2
  let y3, z3;
  if (x1 + x2 === 0) (y3 = y1 + y2), (z3 = z1 + z2);
  else (y3 = y1 - y2), (z3 = z1 - z2);

  //  Divide z3 by y3 which gives y
  const y = z3 / y3;
  //  x = (z1 - y1 * y)/ x1
  const x = (z1 - y1 * y) / x1;

  const formatResult = (num) => {
    if (num.toString().length > 3) return num.toFixed(3);
    return num;
  };
  //  The solutions are x and y
  output.textContent =
    x && y ? `x = ${formatResult(x)}, y = ${formatResult(y)}` : "";
  resetInputFields(); //clear the input field after submission
  e.preventDefault();
}
