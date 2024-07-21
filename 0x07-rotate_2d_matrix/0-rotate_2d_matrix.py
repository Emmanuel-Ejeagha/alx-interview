#!/usr/bin/python3

"""Tech interview matrix problem
[00, 10, 20, 30]
[01, 11, 21, 31]
[02, 12, 22, 32]
[03, 13, 23, 33]


00 -> 03
03 -> 33
33 -> 30
30 -> 00

10 -> 01
01 -> 13
13 -> 31
31 -> 10

20 -> 02
02 -> 23
23 -> 32
32 -> 20

second circle
11 -> 12
12 -> 22
22 -> 21
21 -> 11
"""


def rotate_2d_matrix(matrix):
    """rotate a two D matrix"""

    # length of matrix
    num = len(matrix)

    # loop through each circle
    for i in range(0, int(num/2)):
        # considering the elements in group of 4 in the current circle
        for j in range(i, num-1-i):
            # store the top value in a temp memory
            temp = matrix[i][j]

            # move the left to the top
            matrix[i][j] = matrix[num-1-j][i]

            # move the bottom to the left
            matrix[num-1-j][i] = matrix[num-1-i][num-1-j]

            # move the right to the bottom
            matrix[num-1-i][num-1-j] = matrix[j][num-1-i]

            # move the temp to the right
            matrix[j][num-1-i] = temp
