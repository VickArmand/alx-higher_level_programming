#!/usr/bin/node
const num = Number(process.argv[2]);
if (num) {
  for (let h = 0; h < num; h++) {
    let str = '';
    for (let w = 0; w < num; w++) str = str.concat('X');
    console.log(str);
  }
} else console.log('Missing size');
