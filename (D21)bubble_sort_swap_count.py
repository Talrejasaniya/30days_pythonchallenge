#!/bin/python3

import math
import os
import random
import re
import sys

# Main entry point
if __name__ == '__main__':
    # Read the size of the array
    n = int(input().strip())

    # Read the array elements
    a = list(map(int, input().rstrip().split()))

    # Function to sort array using Bubble Sort and count swaps
    def arr1(a):
        count = 0         # Counter for number of swaps
        n = len(a)

        # Outer loop for passes
        for i in range(n):
            swapped = False  # Track if any swap happened in this pass

            # Inner loop for comparing adjacent elements
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    # Swap and count
                    count += 1
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True

            # If no swaps, the array is already sorted
            if not swapped:
                break

        # Output required results
        print("Array is sorted in", count, "swaps.")
        print("First Element:", a[0])
        print("Last Element:", a[n - 1])

    # Call the function
    arr1(a)
