#!/usr/bin/node
/* Increments value through incr function */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* My code starts here */
myObject.incr = function () {
  myObject.value += 1;
};
/* My code ends here */

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
