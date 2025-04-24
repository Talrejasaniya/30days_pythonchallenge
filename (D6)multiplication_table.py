#!/bin/python3

import math
import os
import random
import re
import sys

# This is the main entry point for the program
if __name__ == '__main__':
    n = int(input().strip())  # Read an integer input and remove any surrounding whitespace

# Loop from 1 to 10 (inclusive)
for i in range(1, 11):
    result = i * n  # Multiply n with the current number i
    # Print the multiplication in a formatted way: "n x i = result"
    print(n, "x", i, "=", result)
