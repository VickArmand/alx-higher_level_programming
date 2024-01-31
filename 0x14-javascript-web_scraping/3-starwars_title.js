#!/usr/bin/node
/*
 * script that prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID
 * You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 */
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
