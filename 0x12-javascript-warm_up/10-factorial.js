#!/usr/bin/node
/* Recursively prints factorial of argv[1] */
const args = process.argv.slice(2);
const num = args[0];
let answer;

if (num) {
  answer = factorial(num);
  console.log(answer);
} else {
  console.log(1);
}

function factorial (num) {
  /* Recursive function to return factorial of num */
  if (num < 0) {
    return (-1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * (factorial(num - 1)));
  }
}
