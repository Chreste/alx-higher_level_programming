#!/usr/bin/node
const fs = require('fs');

const f = fs.readFileSync(process.argv[2]).toString();
const s = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], f + s);
