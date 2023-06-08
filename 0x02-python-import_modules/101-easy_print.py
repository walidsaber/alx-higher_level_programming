#!/usr/bin/python3

if __name__ == "__main__":
    import os

    text = "#pythoniscool\n"
    os.write(1, text.encode())
