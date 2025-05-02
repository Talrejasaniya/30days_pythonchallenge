#!/bin/python3

import math
import os
import random
import re
import sys

# Function to calculate the maximum hourglass sum in a 6x6 2D array
def hourglass_sum(arr):
    # Initialize max_sum with the lowest possible number
    max_sum = float('-inf')
    
    # Loop over possible hourglass top-left positions (0 to 3)
    for i in range(4):
        for j in range(4):
            # Top of hourglass: 3 elements in a row
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            # Middle of hourglass: 1 element
            middle = arr[i+1][j+1]
            # Bottom of hourglass: 3 elements in a row
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            # Total sum of this hourglass
            total = top + middle + bottom
            
            # Update max_sum if this hourglass sum is greater
            max_sum = max(max_sum, total)
    
    return max_sum

if __name__ == '__main__':
    arr = []
    # Read a 6x6 2D array from input
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    # Call the function and print the result
    result = hourglass_sum(arr)
    print(result)
