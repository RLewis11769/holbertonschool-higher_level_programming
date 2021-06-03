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

  print (width, height) {
    /* Prints rectangle with height/width passed in */
    let x;

    for (x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    /* Double height and width of rectangle given */
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    /* Switch values of height and width of rectangle given */
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
