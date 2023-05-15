#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    else:
        for i in matrix:
            for j in i:
                print("{}".format(j), end=" ")
        print("")
