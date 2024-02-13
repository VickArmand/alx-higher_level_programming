#!/usr/bin/node
// jQuery script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (responseData, textStatus) {
  $('UL#list_movies').append(responseData.title);
});
