#!/usr/bin/node

exports.esrever = function (list) {
  /* Returns reversed list (without using reverse method) */
  let x;
  const newList = [];

  for (x = list.length - 1; x >= 0; x--) {
    newList.push(list[x]);
  }
  return newList;
};
