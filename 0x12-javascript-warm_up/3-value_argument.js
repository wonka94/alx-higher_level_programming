#!/usr/bon/node

const { argv } = import('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
