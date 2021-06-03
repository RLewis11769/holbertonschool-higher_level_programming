#!/usr/bin/node
/* Executes function passed from 101main.js number of times passed in */
exports.callMeMoby = function (num, func) {
  let x;

  for (x = 0; x < num; x++) {
    func();
  }
};
