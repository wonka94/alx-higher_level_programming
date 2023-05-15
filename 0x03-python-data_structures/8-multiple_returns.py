#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first = sentence[0]
    else:
        first = None
        length = len(sentence)
    return (length, first)