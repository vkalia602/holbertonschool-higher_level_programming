#!/usr/bin/node
// script that prints the title of a Star Wars movie with swapi

let counter = 0;
let characslist = [];
let movieinfo = [];
let request = require('request');
let search = 'https://swapi.co/api/people/18/';
let search2 = 'http://swapi.co/api/people/18/';
let requestURL = process.argv[2];

request(requestURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    movieinfo = (JSON.parse(body)['results']);
    for (let i = 0; i < movieinfo.length; i++) {
      characslist = movieinfo[i]['characters'];
      if (characslist.indexOf(search) > -1 || characslist.indexOf(search2) > -1) {
        counter++;
      }
    }
    console.log(counter);
  }
});
