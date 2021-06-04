#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  /* Prints argument passed in and total number of arguments printed so far */
  console.log(count + ': ' + item);
  count++;
};
