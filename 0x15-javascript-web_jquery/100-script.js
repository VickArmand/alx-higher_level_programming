#!/usr/bin/nod
// JavaScript script that updates the text color of the <header> element to red (#FF0000)
// Note: Your script must be imported from the <head> tag, not at the end of the HTML
window.onload = function () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
};
