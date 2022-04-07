#!/usr/bin/node

let x = 1;
process.argv.forEach((value, index) => {
  x++;
});

if (x > 3) { console.log(process.argv[2]); } else { console.log('No argument'); }
