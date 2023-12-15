#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const index in list) {
    if (list[index] === searchElement) occurences += 1;
  }
  return occurences;
};
