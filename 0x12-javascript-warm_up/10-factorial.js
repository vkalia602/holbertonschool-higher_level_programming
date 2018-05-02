#!/usr/bin/node
function factorial (a) {
  if (a === 0) { return (1); }
  return (factorial(a - 1) * a);
}
let num = parseInt(process.argv[2]);
if (typeof (num) === 'number' && !isNaN(num)) {
  console.log(factorial(num));
} else {
  console.log(factorial(1));
}
