#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

let request = require('request');
let requestURL = process.argv[2];
let fileto = process.argv[3];
let fs = require('fs');

request(requestURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileto, body, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
