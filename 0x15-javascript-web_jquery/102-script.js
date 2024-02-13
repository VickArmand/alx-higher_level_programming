#!/usr/bin/node
// jQuery script that fetches and prints how to say “Hello” depending on the language
// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
// You script must work when imported from the <head> tag
$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=';
    $.get(url + code, function (responseData, textstatus) {
      $('DIV#hello').text(responseData.hello);
    });
  });
});
