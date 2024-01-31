#!/usr/bin/node
/*
 * script that gets the contents of a webpage and stores it in a file.
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 */
const req = require('request');
const fs = require('fs');
req(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
