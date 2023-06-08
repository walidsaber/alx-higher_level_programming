#!/usr/bin/python3

if __name__ == "__main__":
    import sys

<<<<<<< HEAD
    def args_counts():
        args = sys.argv[1:]
        argc = len(args)
        if argc > 0:
            dot = ":"
        else:
            dot = ""
        print(f"{argc} arguments{dot}")
        for i in range(len(args)):
            print("i: {args[i]}")
=======
def args_counts():
    args = sys.argv[1:]
    argc = len(args)
    if argc > 0:
        dot = ":"
    else:
        dot = ""
    print(f"{argc} arguments{dot}")
    for i in range(len(args)):
        print(f"{i+1}: {args[i]}")
>>>>>>> 1497edb40040cebf2067265d3292b11677202e37

args_counts()
