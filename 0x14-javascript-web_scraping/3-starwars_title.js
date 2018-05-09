#!/usr/bin/node
// script that prints the title of a Star Wars movie with swapi

let requestURL = 'http://swapi.co/api/films/' + process.argv[2];
let request = require('request');

request(requestURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body)['title']);
  }
});
