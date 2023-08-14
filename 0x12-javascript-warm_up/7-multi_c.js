#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const value = parseInt(argv[2]);
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
