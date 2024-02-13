#!/usr/bin/node
// jQuery script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (responseData, textStatus) {
  $('DIV#hello').append(responseData.hello);
});
