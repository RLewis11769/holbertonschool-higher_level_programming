#!/usr/bin/node
/* If argv[1] is integer (even if string), prints, otherwise prints "Not a number" */
const args = process.argv.slice(2);
if (parseInt(args[0])) {
  console.log('My number: ' + args[0]);
} else {
  console.log('Not a number');
}
