#!/usr/bin/node
/* Increments number passed in by 1 */
exports.addMeMaybe = function (num, func) {
  return func(num + 1);
};
