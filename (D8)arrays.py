#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read an integer n (number of elements to reverse)
    n = int(input().strip())
    
    # Read a list of integers from input, splitting the line into numbers
    arr = list(map(int, input().strip().split()))
    
    # Take only the first n elements (in case more numbers are entered)
    arr = arr[:n]
    
    # Reverse the list
    arr.reverse()
    
    # Print the reversed list elements, space-separated
    print(*arr)
