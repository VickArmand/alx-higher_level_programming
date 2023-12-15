#!/usr/bin/node
const data = require('./101-data').dict;
const newdata = {};
for (const key in data) {
  if (newdata[data[key]]) newdata[data[key]].push(key);
  else newdata[data[key]] = [key];
}
console.log(newdata);
