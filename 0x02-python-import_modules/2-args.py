#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    print("{}: arguments".format(len(arguments) - 1))
    for i in range(1, len(arguments)):
        print("{}: {}".format(i, arguments[i]))
