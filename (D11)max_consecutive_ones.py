#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

# Convert to binary and remove the '0b' prefix
binary = bin(n)[2:]

# Print the binary representation (optional)

# Split the binary string by '0' to get sequences of 1s
groups = binary.split('0')

# Find the maximum length of consecutive 1s
max_consecutive_ones = max(len(group) for group in groups)

# Print the result
print( max_consecutive_ones)

       
        
