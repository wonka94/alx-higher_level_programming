#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
