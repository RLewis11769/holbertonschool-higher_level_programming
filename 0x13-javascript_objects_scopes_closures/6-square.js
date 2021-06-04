#!/usr/bin/node

/* Imports Rectangle class */
const Square5 = require('./5-square');

class Square extends Square5 {
/* Defines methods and attributes of Square class that inherits from Square in 5-square.js that inherits from Rectangle */

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
