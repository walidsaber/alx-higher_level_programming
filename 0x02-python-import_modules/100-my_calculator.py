#!/usr/bin/python3

if __name__ == "__main__":
    """"importing basic calculations"""
    from calculator_1 import add, sub, mul, div
    import sys

    def userinp():
        args = sys.argv[1:]
        arg_count = len(args)

        if arg_count != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        a = args[0]
        b = args[2]
        if args[1] == "+":
            operator = '+'
        elif args[1] == "-":
            operator = '-'
        elif args[1] == "*":
            operator = '*'
        elif args[1] == "/":
            operator = '/'
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        result = eval(f"{a} {operator} {b}")
        print(f"{a} {operator} {b} = {result}")
    userinp()
