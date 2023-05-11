#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    operators = "+-/*"
    if(len(sys.argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if(operator in operators):
            if(operator == "+"):
                print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            elif(operator == "-"):
                print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            elif(operator == "/"):
                print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            else:
                print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
