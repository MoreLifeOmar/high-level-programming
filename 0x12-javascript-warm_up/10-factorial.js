#!/usr/bin/node

console.log(factorial(parseInt(process.argv[2])));

function factorial (a) {
  if (isNaN(a) || a === 1) { return 1; }
  return a * (factorial(a - 1));
}
