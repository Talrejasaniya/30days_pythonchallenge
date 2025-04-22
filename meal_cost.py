#!/bin/python3

import math
import os
import random
import re
import sys

# This function calculates the total meal cost, including tip and tax,
# and rounds it to the nearest integer according to standard rounding rules.
def solve(meal_cost, tip_percent, tax_percent):
    # Calculate the tip and tax amounts
    tip = (tip_percent / 100) * meal_cost
    tax = (tax_percent / 100) * meal_cost
    
    # Calculate the total cost of the meal
    total_cost = meal_cost + tip + tax
    
    # Round the total cost to the nearest integer
    if total_cost - int(total_cost) < 0.5:
        print(int(total_cost))  # Round down
    else:
        print(math.ceil(total_cost))  # Round up

if __name__ == '__main__':
    # Take inputs for meal cost, tip percentage, and tax percentage
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    
    # Call the solve function with the provided inputs
    solve(meal_cost, tip_percent, tax_percent)
