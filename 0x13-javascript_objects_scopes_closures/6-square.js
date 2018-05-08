#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let strn = '';
      for (let j = 0; j < this.width; j++) {
        strn = strn + c;
      }
      console.log(strn);
    }
  }
}
module.exports = Square;
