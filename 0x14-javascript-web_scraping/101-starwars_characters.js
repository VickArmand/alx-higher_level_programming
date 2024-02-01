#!/usr/bin/node
/*
 *  script that prints all characters of a Star Wars movie:
 *  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 *  Display one character name by line in the same order of the list “characters” in the /films/ response
 *  You must use the Star wars API
 */
const req = require('request');
const filmsUrl = 'https://swapi-api.alx-tools.com/api/films/';
const peopleUrl = 'https://swapi-api.alx-tools.com/api/people/';
function sortUrlArray (urlArray) {
  for (const index in urlArray) {
    urlArray[index] = urlArray[index].replace(peopleUrl, '').replace('/', '');
    urlArray[index] = Number(urlArray[index]);
  }
  return urlArray.sort((a, b) => a - b);
}
req(filmsUrl + process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    const filmCharacters = sortUrlArray(JSON.parse(body).characters);
    for (const index in filmCharacters) {
      req(peopleUrl + filmCharacters[index], (error, response, body) => {
        if (error) console.log(error);
        else {
          const characters = JSON.parse(body);
          console.log(characters.name);
        }
      });
    }
  }
});
