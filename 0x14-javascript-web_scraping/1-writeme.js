#!/usr/bin/node
// Script that writes a string to a file

let filename = process.argv[2];
let fs = require('fs');

fs.writeFile(filename, process.argv[3], 'utf8', (err) => {
  if (err) { console.log(err); }
});
