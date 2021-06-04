#!/usr/bin/node

exports.converter = function (base) {
  /* Returns return of myConverter function */

  function myConverter (num) {
    /* Returns num converted to base */
    return num.toString(base);
  }
  return myConverter;
};
