"using strict";

/*
SIMULTANEOUS EQUATION SOLVER

E.g of a simultaneous equation
x + y = 8
2x + 5y = 14
find the values of x and y
*/

let sign00,
  sign01,
  x1Coef,
  y1Coef,
  sign0,
  x1y1Result,
  sign10,
  sign11,
  x2Coef,
  y2Coef,
  sign1,
  x2y2Result,
  x1CoefPositive,
  x2CoefPositive,
  y1CoefPositive,
  y2CoefPositive,
  xCoef,
  yCoef,
  xResult,
  yResult,
  totalResult,
  xNewEqn,
  yNewEqn,
  numX,
  numY,
  numX1,
  numY1,
  numResult,
  newResult1;

const userInput = function () {
  sign00 = prompt("Input the sign for X1 (+ or -): ");
  x1Coef = Number(prompt("Input the Coefficient of X in equation1: "));
  sign01 = prompt("Input the sign for Y1 (+ or -): ");
  y1Coef = Number(prompt("Input the Coefficient of Y in equation1: "));
  sign0 = prompt("Input the sign of the result of eqn1: ");
  x1y1Result = Number(prompt("Input the result of eqn1: "));
  sign10 = prompt("Input the sign for X2 (+ or -): ");
  x2Coef = Number(prompt("Input the Coefficient of X in equation2: "));
  sign11 = prompt("Input the sign for Y2 (+ or -): ");

  y2Coef = Number(prompt("Input the Coefficient of Y in equation2: "));
  sign1 = prompt("Input the sign of the result of eqn2: ");
  x2y2Result = Number(prompt("Input the result of eqn2: "));
};

userInput();

if (sign00 === "-") {
  x1Coef = -x1Coef;
} else if (!sign00 === "-" || !sign00 === "+") {
  alert("Invalid sign, refresh the page to start again!");
}

if (sign01 === "-") {
  y1Coef = -y1Coef;
} else if (!sign01 === "-" || !sign00 === "+") {
  alert("Invalid sign, refresh the page to start again!");
}

if (sign0 === "-") {
  x1y1Result = -x1y1Result;
} else if (!sign0 === "-" || !sign00 === "+") {
  alert("Invalid sign, refresh the page to start again!");
}

if (sign10 === "-") {
  x2Coef = -x2Coef;
} else if (!sign10 === "-" || !sign00 === "+") {
  alert("Invalid sign, refresh the page to start again!");
}

if (sign11 === "-") {
  y2Coef = -y2Coef;
} else if (!sign10 === "-" || !sign00 === "+") {
  alert("Invalid sign, refresh the page to start again!");
}

if (sign1 === "-") {
  x2y2Result = -x2y2Result;
} else if (!sign1 === "-" || !sign00 === "+") {
  alert("Invalid sign, refresh the page to start again!");
}

// Convert the integers to strings so that the equations can be printed
let showX1 = String(x1Coef) + "x";
let showY1 = String(y1Coef) + "y";
let showX2 = String(x2Coef) + "x";
let showY2 = String(y2Coef) + "y";
let showEqn1 = String(x1y1Result);
let showEqn2 = String(x2y2Result);

// Showing an alert for confirmation of the equation

if (sign01 === "+") {
  alert(`${showX1} + ${showY1} = ${showEqn1} ------ (1)`);
} else if (sign01 === "-") {
  alert(`${showX1}${showY1} = ${showEqn1} ------ (1)`);
}
if (sign11 === "+") {
  alert(`${showX2} + ${showY2} = ${showEqn2} ------ (2)`);
} else if (sign11 === "-") {
  alert(`${showX2} ${showY2} = ${showEqn2} ------ (2)`);
}

// Using elimination method
// Convert the coefficients of each variable to positive so that there can be easy comparison of the coefficients of the variables

if (y1Coef < 0) {
  y1CoefPositive = -1 * y1Coef;
} else {
  y1CoefPositive = y1Coef;
}

if (y2Coef < 0) {
  y2CoefPositive = -1 * y2Coef;
} else {
  y2CoefPositive = y2Coef;
}

if (x1Coef < 0) {
  x1CoefPositive = -1 * x1Coef;
} else {
  x1CoefPositive = x1Coef;
}

if (x2Coef < 0) {
  x2CoefPositive = -1 * x2Coef;
} else {
  x2CoefPositive = x2Coef;
}

// Using elimination method if the coefficients of y are the same but with different signs (e.g + and -)
if (y1CoefPositive === y2CoefPositive && sign01 !== sign11) {
  // Add the coefficients of x together after eliminating y
  xCoef = x1Coef + x2Coef;

  // Add the results of both equations
  totalResult = x1y1Result + x2y2Result;

  // Divide the added result by the added coefficients of x to get the total value of x
  xResult = totalResult / xCoef;
  alert(`f(x) = ${xResult}`);

  // Finding the value of y
  // Multiply the coefficient of x in eqn 1 by the value of x gotten from the result
  xNewEqn = x1Coef * xResult;

  // Check to see if the new number gotten from the multiplication of x & its coefficient is negative. Then change the sign to the opposite when taking it to the other side of the equal sign
  if (xNewEqn < 0) {
    newResult1 = x1y1Result + -xNewEqn;
  } else {
    // If the new eqn is positive, it is subtracted from the equation value of eqn(1)
    newResult1 = x1y1Result - xNewEqn;
  }
  yResult = newResult1 / y1Coef;
  alert(`f(y) = ${yResult}`);
  // If the signs of the coefficients of y are the same, then
} else if (y1CoefPositive === y2CoefPositive && sign01 === sign11) {
  xCoef = x2Coef - x1Coef;
  totalResult = x2y2Result - x1y1Result;
  xResult = totalResult / xCoef;
  alert(`f(x) = ${xResult}`);

  xNewEqn = x1Coef * xResult;
  if (xNewEqn < 0) {
    newResult1 = x1y1Result + -xNewEqn;
  } else {
    newResult1 = x1y1Result - xNewEqn;
  }
  yResult = newResult1 / y1Coef;
  alert(`f(y) = ${yResult}`);
} else if (x1CoefPositive === x2CoefPositive && sign00 !== sign10) {
  yCoef = y1Coef + y2Coef;
  totalResult = x1y1Result + x2y2Result;
  yResult = totalResult / yCoef;
  alert(`f(y) = ${yResult}`);
  yNewEqn = y1Coef * yResult;

  if (yNewEqn < 0) {
    newResult1 = x1y1Result + -yNewEqn;
  } else {
    newResult1 = x1y1Result - yNewEqn;
  }
  xResult = newResult1 / x1Coef;
  alert(`f(x) = ${xResult}`);
} else if (x1CoefPositive === x2CoefPositive && sign00 === sign10) {
  yCoef = y2Coef - y1Coef;
  totalResult = x2y2Result - x1y1Result;
  yResult = totalResult / yCoef;
  alert(`f(y) = ${yResult}`);

  yNewEqn = y1Coef * yResult;
  if (yNewEqn < 0) {
    newResult1 = x1y1Result + -yNewEqn;
  } else {
    newResult1 = x1y1Result - yNewEqn;
  }
  xResult = newResult1 / x1Coef;
  alert(`f(x) = ${xResult}`);
} else if (
  x1CoefPositive !== x2CoefPositive &&
  y1CoefPositive !== y2CoefPositive
) {
  // Using substitution method
  // This block will run when the coefficients of either variables are not the same
  if (x1CoefPositive === 1) {
    numResult = x2Coef * x1y1Result;
    numY1 = x2Coef * -y1Coef;
    numY = numY1 + y2Coef;
    numY = -numY;
    newResult1 = numResult - x2y2Result;
    yResult = newResult1 / numY;
    xResult = x1y1Result - y1Coef * yResult;
    alert(`f(y) = ${yResult}
    f(x) = ${xResult}`);
  } else if (y1CoefPositive === 1) {
    numResult = y2Coef * x1y1Result;
    numX1 = y2Coef * -x1Coef;
    numX = numX1 + x2Coef;
    numX = -numX;
    newResult1 = numResult - x2y2Result;
    xResult = newResult1 / numX;
    yResult = x1y1Result - x1Coef * xResult;
    alert(`f(x) = ${xResult}
    f(y) = ${yResult}`);
  } else if (x2CoefPositive === 1) {
    numResult = x1Coef * x2y2Result;
    numY1 = x1Coef * -y2Coef;
    numY = numY1 + y1Coef;
    numY = -numY;
    newResult1 = numResult - x1y1Result;
    yResult = newResult1 / numY;
    xResult = x2y2Result - y2Coef * y;
    alert(`f(y) = ${yResult}
    f(x) = ${xResult}`);
  } else if (y2CoefPositive === 1) {
    numResult = y1Coef * x2y2Result;
    numX1 = y1Coef * -x2Coef;
    numX = numX1 + x1Coef;
    numX = -numX;
    newResult1 = numResult - x1y1Result;
    xResult = newResult1 / numX;
    yResult = x2y2Result - x2Coef * xResult;
  } else {
    xUpper = x1y1Result * y2Coef - x2y2Result * y1Coef;
    xLower = x1Coef * y2Coef - x2Coef * y1Coef;
    xResult = xUpper / xLower;
    yResult = (x1y1Result - x1Coef * xResult) / y1Coef;
    alert(`f(x) = ${xResult}
    f(y) = ${yResult}`);
  }
}
