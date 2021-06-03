#!/usr/bin/node

class Rectangle {
/* Defines methods and attributes of Rectangle class */

  constructor (w, h) {
    /* Constructor function to validate data and create new instance of Rectangle */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
