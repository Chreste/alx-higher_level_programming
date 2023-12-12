#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let y = 0; y < list.length; y++) {
    if (searchElement === list[y]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
