#!/usr/bin/node
/*
 * script that reads and prints the content of a file.
 * first argument is the file path
 */
const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
