#!/usr/bin/node
/* Print string statements argv[1] number of times */
const args = process.argv.slice(2);
const num = args[0];
let x;

if (num === 0) {
  console.log('Missing number of occurrences');
}
for (x = 0; x < num; x++) {
  console.log('C is fun');
}
