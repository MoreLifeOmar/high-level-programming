#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const value of Object.values(dict)) {
  const newList = [];
  newDict[value] = newList;
  for (const k in dict) {
    if (dict[k] === Number(value)) {
      newList.push(k);
    }
  }
}
console.log(newDict);
