#!/usr/bin/node

/* Imports Rectangle class */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
/* Defines methods and attributes of Square class that inherits from Rectangle */

  constructor (size) {
    /* Constructor function to create new instance of Square through Rectangle attributes and methods */
    super(size, size);
  }

  charPrint (c) {
    /* Prints square of character passed in with size passed in */
    let x;
    let char = 'X';

    if (c) {
      char = c;
    }

    for (x = 0; x < this.width; x++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
