#!/usr/bin/node
// jQuery script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (responseData, textStatus) {
  $.each(responseData.results, function (index, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
