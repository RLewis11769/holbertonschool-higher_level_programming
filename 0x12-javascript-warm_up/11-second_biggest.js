#!/usr/bin/node
/* Print second-largest int in argv */
const args = process.argv.slice(2);

if (args.length === 1) {
  console.log(0);
} else if (args[0]) {
  console.log(secondLargest(args));
} else {
  console.log(0);
}

function secondLargest (arr) {
  let max = -Infinity;
  let result = -Infinity;
  let x;
  let num;

  for (x of arr) {
    num = Number(x);
    if (num > max) {
      [result, max] = [max, num]; // save previous max
    } else if (num < max && num > result) {
      result = num; // new second biggest
    }
  }
  return result;
}
