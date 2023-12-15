#!/usr/bin/node
const data = require('./100-data.js').list;
console.log(data);
const newdata = data.map((element, index) => element * index);
console.log(newdata);
