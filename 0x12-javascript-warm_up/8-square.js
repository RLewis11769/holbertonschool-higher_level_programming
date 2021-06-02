#!/usr/bin/node
/* Print string statements argv[1] number of times */
const args = process.argv.slice(2);
const num = args[0];
let x;
let string = '';

if (parseInt(num)) {
  for (x = 0; x < num; x++) {
    string += 'X';
  }
  for (x = 0; x < string.length; x++) {
    console.log(string);
  }
} else {
  console.log('Missing size');
}
