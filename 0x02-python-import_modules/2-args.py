#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    end = ""
    args = ""
    if (sys.argv == 1):
        args = "argument"
    else:
        args = "arguments"
    if (sys.argv  == 0):
        end = "."
    else:
        end = ":"
    print("{} {}{}".format(len(sys.argv) - 1), args, end)
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
