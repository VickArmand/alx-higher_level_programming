#!/usr/bin/node
// jQuery script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (responseData, textStatus) {
  $('DIV#character').text(responseData.name);
});
