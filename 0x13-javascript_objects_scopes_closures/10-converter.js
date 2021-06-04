#!/usr/bin/node

exports.converter = function (base) {
  /* Returns number in base passed in */
  function myConverter (num) {
    return num.toString(base);
  }
  return myConverter;

};
