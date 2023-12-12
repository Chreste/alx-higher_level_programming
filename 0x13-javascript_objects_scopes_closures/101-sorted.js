#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const x in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[x]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valsUniq[x]] = list;
}
console.log(newDict);
