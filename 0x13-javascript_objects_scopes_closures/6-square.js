#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
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
