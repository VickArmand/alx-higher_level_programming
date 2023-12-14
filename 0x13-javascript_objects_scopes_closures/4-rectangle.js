#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      let str = '';
      for (let w = 0; w < this.width; w++) str = str.concat('X');
      console.log(str);
    }
  }

  rotate () {
    const buffer = this.width;
    this.width = this.height;
    this.height = buffer;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
