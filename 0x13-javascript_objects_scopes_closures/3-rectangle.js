#!/usr/bin/node
// class Rectangle that defines a rectangle with print method

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let strn = '';
      for (let j = 0; j < this.width; j++) {
        strn = strn + 'X';
      }
      console.log(strn);
    }
  }
}
module.exports = Rectangle;
