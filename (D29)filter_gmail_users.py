#!/bin/python3

# Import required modules
import math
import os
import random
import re  # Regular expressions module
import sys

# Main function starts here
if __name__ == '__main__':
    # Read the number of entries (rows)
    N = int(input().strip())
    
    # Initialize an empty list to store first names with Gmail accounts
    result = []

    # Loop through each entry
    for _ in range(N):
        # Split the input into firstName and emailID
        firstName, emailID = input().strip().split()

        # Check if the emailID ends with '@gmail.com' using regex
        if re.search(r'@gmail\.com$', emailID):
            # If it matches, add the first name to the result list
            result.append(firstName)

    # Sort the list of first names alphabetically
    for name in sorted(result):
        # Print each name on a new line
        print(name)
