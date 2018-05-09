#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

let request = require('request');
let requestURL = process.argv[2];
let datadict = {};
let userlist = [];

request(requestURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    userlist = JSON.parse(body);
    for (let i = 0; i < userlist.length; i++) {
      let user = userlist[i]['userId'];
      if (userlist[i]['completed'] === true) {
        if (!(user in datadict)) {
          datadict[user] = 1;
        } else {
          datadict[user] += 1;
        }
      }
    }
  }
  console.log(datadict);
});
