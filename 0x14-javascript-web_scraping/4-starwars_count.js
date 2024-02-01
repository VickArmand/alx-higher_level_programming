#!/usr/bin/node
/*
 * script that prints the number of movies where the character “Wedge Antilles” is present.
 * The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 */
const req = require('request');
const url = process.argv[2];
const str = 'https://swapi-api.alx-tools.com/api/people/18/';
req(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    let count = 0;
    const films = JSON.parse(body);
    for (const index in films.results) {
      if (films.results[index].characters.includes(str)) count++;
    }
    console.log(count);
  }
});
