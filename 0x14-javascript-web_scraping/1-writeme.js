#!/usr/bin/node
/*
 * script that writes a string to a file
 * first argument is the file path
 * second argument is the string to write
 */
const filesystem = require('fs');
filesystem.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
