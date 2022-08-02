#!/usr/bin/node
let idx = 0;
exports.logMe = function (item) {
  console.log(idx + ': ' + item);
  idx++;
};
