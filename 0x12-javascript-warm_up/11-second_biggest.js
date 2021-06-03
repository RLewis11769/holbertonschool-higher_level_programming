#!/usr/bin/node
/* Print second-largest int in argv */
const args = process.argv.slice(2);

if (args.length === 1) {
  console.log(0);
} else if (args[0]) {
  console.log(second(args));
} else {
  console.log(0);
}

function second (arr) {
  let max = -Infinity;
  let result = -Infinity;
  let x, num;

  for (x = 0; x < arr.length; x++) {
    num = Number(arr[x]);
    if (num > max) {
      [result, max] = [max, num];
    } else {
      result = num;
    }
  }
  return (result);
}
