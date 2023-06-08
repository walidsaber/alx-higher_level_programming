#!/usr/bin/python3

if __name__ == "__main__":
    import os

    text = "#pythoniscool"
    os.write(1, text.encode())
