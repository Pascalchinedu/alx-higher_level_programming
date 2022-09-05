#!/usr/bin/node
const numj = Number.parseInt(process.argv[2]);

console.log(Number.isNaN(numj) ? 'Not a number' : 'My number: ' + numj);
