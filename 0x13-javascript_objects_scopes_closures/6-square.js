#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let x = '';
      for (let i = 0; i < this.width; i++) {
        x += c;
      }
      for (let l = 0; l < this.height; l++) {
        console.log(x);
      }
    }
  }
};
