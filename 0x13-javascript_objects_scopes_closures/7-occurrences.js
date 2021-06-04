#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  /* Return count for each instance of searchElement in list */
  let x;
  let count = 0;

  for (x in list) {
    if (list[x] === searchElement) {
      count++;
    }
  }
  return count;
};
