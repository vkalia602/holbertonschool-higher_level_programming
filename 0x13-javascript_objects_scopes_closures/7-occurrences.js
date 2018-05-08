#!/usr/bin/node
// Function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  var counter = 0;

  for (var i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return (counter);
};
