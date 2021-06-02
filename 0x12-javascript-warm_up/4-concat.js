#!/usr/bin/node
/* Prints sentence of argv[1] is argv[2] if exist, otherwise "undefined" */
const args = process.argv.slice(2);
let first = 'undefined';
let second = 'undefined';
if (args[0]) {
  first = args[0];
}
if (args[1]) {
  second = args[1];
}
console.log(first + ' is ' + second);
