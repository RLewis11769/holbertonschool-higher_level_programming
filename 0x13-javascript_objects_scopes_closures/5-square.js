#!/usr/bin/node

/* Imports Rectangle class */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
/* Defines methods and attributes of Square class that inherits from Rectangle */

  constructor (size) {
    /* Constructor function to create new instance of Square through Rectangle attributes and methods */
    super(size, size);
  }
}

module.exports = Square;
