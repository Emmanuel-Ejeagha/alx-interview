#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """Rotates a two D matrix"""
    
    # length of matrix
    num = len(matrix)
    
    # loop through each circle
    for i in range(0, int(num/2)):
        # considering the elements in group of 4 in the current circle
        for j in range(i, num-1-i):
            # considering the elemr=ents in group of 4 in the current circle
            for j in range(i, num-1-i):
                # store the top value in a temp memory
                temp = matrix[i][j]
                # move the left to the to the top
                matrix[i][j] = matrix[num-1-j][i]
                
                # move the bottom to the left
                matrix[num-1-j][i] = matrix[num-1-i][num-1-j]
                
                # move the right to the bottom
                matrix[num-1-i][num-1-j] = matrix[j][num-1-i]
                
                # move the temp to the right
                matrix[j][num-1-i] = temp

            