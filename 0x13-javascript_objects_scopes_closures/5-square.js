#!/usr/bin/node

/* Imports Rectangle class */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
/* Defines methods and attributes of Square class that inherits from Rectangle */

  constructor (size) {
    /* Constructor function to validate data and create new instance of Square */
    if (size > 0) {
      super(size, size);
    }
  }
}

module.exports = Square;
