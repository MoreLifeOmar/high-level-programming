#!/usr/bin/node
const dict = require('./101-data').dict;
const dictOcc = {};
for (const key in dict) {
  if (dictOcc[dict[key]] === undefined) { dictOcc[dict[key]] = []; }
  dictOcc[dict[key]].push(key);
}
console.log(dictOcc);
