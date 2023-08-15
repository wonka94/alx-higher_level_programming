#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const occurence = list.filter(item => item === searchElement);
  return occurence.length;
};
