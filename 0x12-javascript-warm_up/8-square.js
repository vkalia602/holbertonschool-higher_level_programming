#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (typeof (num) === 'number' && !isNaN(num)) {
  let i = num;
  let j = num;
  let strng;
  for (; i > 0; i--) {
    strng = '';
    for (j = process.argv[2]; j > 0; j--) {
      (strng = strng + 'X');
    }
    console.log(strng);
  }
} else if (num < 0) {
} else {
  console.log('Missing size');
}
