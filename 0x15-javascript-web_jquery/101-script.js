#!/usr/bin/node
// jQuery script that adds, removes and clears LI elements from a list
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
// When the user clicks on DIV#add_item: a new element is added to the list
// When the user clicks on DIV#remove_item: the last element is removed from the list
// When the user clicks on DIV#clear_list: all elements of the list are removed
$(window).on('load', function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list LI').first().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list LI').remove();
  });
});
