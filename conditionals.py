import math
import os
import random
import re
import sys

# Check the value of N and print appropriate response based on conditions
if __name__ == '__main__':
    # Read the integer input
    N = int(input().strip())

    # If N is odd, print "Weird"
    if N % 2 != 0:
        print("Weird")
    # If N is even, check further conditions
    elif N % 2 == 0:
        # Check for the range of N
        if 2 <= N <= 5:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
