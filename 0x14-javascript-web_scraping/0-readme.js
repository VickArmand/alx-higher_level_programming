#!/usr/bin/node
const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
