#!/usr/bin/node
/*
 * script that display the status code of a GET request.
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 */
const req = require('request');
req(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  console.log('code: ' + response.statusCode);
}
);
