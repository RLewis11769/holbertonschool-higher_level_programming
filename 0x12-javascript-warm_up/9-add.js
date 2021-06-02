#!/usr/bin/node
/* Prints sum of argv[1] and argv[2] if exist */
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log('NaN');
} else {
  console.log(parseInt(args[0]) + parseInt(args[1]));
}
