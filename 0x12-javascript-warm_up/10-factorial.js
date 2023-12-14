#!/usr/bin/node
function factorial (num) {
  if (num <= 1) return (1);
  else return (num * factorial(num - 1));
}
const num = Number(process.argv[2]);
if (num) console.log(factorial(num));
else console.log(1);
