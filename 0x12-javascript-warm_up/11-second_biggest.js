#!/usr/bin/node
const arr = [];
let len = 0;
if (process.argv.length <= 3) console.log(0);
else {
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
    len += 1;
  }
  arr.sort((x, y) => { return (x - y); });
  console.log(arr[len - 2]);
}
