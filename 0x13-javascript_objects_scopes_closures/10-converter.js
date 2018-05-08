#!/usr/bin/node
// Function that converts a number from base 10 to another base passed as arg
exports.converter = function (base) {
  function convert (number) {
    return (number.toString(base));
  }
  return (convert);
};
