for x in range(0, 10):
    for i in range(x, 9):
        if (x != 8):
            print("{}{}, ".format(x, i+1), end='')
        else:
             print("{}{}".format(x, i+1), end='')