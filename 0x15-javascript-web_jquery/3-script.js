#!/usr/bin/node
// jQuery script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header
$('DIV#red_header').click(function () {
  if ($('header').hasClass('red') === false) {
    $('header').addClass('red');
  }
});
