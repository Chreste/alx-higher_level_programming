#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let y = list.length - 1; y >= 0; y--) {
    newList.push(list[y]);
  }
  return newList;
};
