#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    def args_counts():
        args = sys.argv[1:]
        argc = len(args)
        result = 0
        for i in range(argc):
            result += int(args[i])
        print(result)
args_counts()
