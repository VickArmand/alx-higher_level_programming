#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  for (let i = 0; i < len / 2; i++) {
    const buffer = list[i];
    list[i] = list[len - 1 - i];
    list[len - 1 - i] = buffer;
  }
  return list;
};
