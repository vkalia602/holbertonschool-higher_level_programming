#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  let arr = [];
  let num;
  while (process.argv[i] !== undefined) {
    num = parseInt(process.argv[i]);
    arr.push(num);
    i++;
  }
  arr.sort();
  let set1 = new Set(arr);
  let array = Array.from(set1);
  num = ((array.length) - 2);
  console.log(array[num]);
}
