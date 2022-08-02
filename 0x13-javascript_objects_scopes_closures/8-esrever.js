#!/usr/bin/node
exports.esrever = function (list) {
  // const array = [];
  // for (let i = list.length - 1; i >= 0; i--) {
  //  array.push(list[i]);
  // }
  // return array;
  for (let i = 0, j = list.length - 1; i < list.length / 2; i++, j--) {
    // [list[i] = list[j]] = [list[j] = list[i]];
    const tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
  }
  return list;
};
