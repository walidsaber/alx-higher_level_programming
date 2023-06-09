#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 1
        for x in i:
            print(f"{x}", end="")
            if count == len(i):
                pass
            else:
                print(" ", end="")
            count += 1
        print("")
