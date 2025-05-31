#!/bin/python3

import os
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N : upper limit of numbers (1 to N)
#  2. INTEGER K : the limit that bitwise AND result should be less than
#

def bitwiseAnd(N, K):
    # Check if K-1 can be obtained as a & b with a,b ≤ N.
    # If yes, return K-1 since it's the maximum value less than K.
    if ((K - 1) | K) <= N:
        return K - 1
    else:
        # Otherwise, return K-2, which will be the next best possible value.
        return K - 2

if __name__ == '__main__':
    t = int(input().strip())  # Number of test cases

    # Detect if running on HackerRank (with OUTPUT_PATH env variable) or locally
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        # Function to write output to file (HackerRank)
        write_output = lambda x: fptr.write(str(x) + '\n')
    else:
        # Function to print output to console (local run)
        write_output = lambda x: print(x)

    for _ in range(t):
        # Read two integers: N and K for each test case
        first_multiple_input = input().rstrip().split()
        N = int(first_multiple_input[0])
        K = int(first_multiple_input[1])

        # Get the result using the bitwiseAnd function
        result = bitwiseAnd(N, K)

        # Output the result appropriately
        write_output(result)

    if 'OUTPUT_PATH' in os.environ:
        fptr.close()
