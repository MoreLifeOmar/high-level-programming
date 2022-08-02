#!/usr/bin/node
const fs = require('fs');
const fileA = (process.argv[2].toString());
const fileB = (process.argv[3].toString());
const data = fs.readFileSync(fileA, 'utf-8');
const datab = fs.readFileSync(fileB, 'utf-8');
const msg = data + datab;
fs.writeFile(process.argv[4].toString(), msg, function (err) {
  if (err) {
    return console.log(err);
  }
});
