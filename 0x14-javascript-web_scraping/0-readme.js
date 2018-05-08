#!/usr/bin/node
// Function that reads a file and prints the contents of the file on stdout

let filename = process.argv[2];
let fs = require('fs');

fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
  if (data) {
    console.log(data);
  }
});
