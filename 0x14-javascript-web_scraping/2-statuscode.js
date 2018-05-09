#!/usr/bin/node
// Script that display the status code of a GET request

let requestURL = process.argv[2];
let request = require('request');

request(requestURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
