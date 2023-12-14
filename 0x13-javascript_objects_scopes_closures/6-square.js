#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let h = 0; h < this.height; h++) {
      let str = '';
      for (let w = 0; w < this.width; w++) {
        if (c) str = str.concat(c);
        else str = str.concat('X');
      }
      console.log(str);
    }
  }
};
