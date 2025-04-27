# Import sys to read input until EOF
import sys

# Read the number of (name, number) pairs to be added to the phonebook
n = int(input())
phonebook = {}

# Build the phonebook dictionary
for _ in range(n):
    name, number = input().split()  # Split input into name and number
    phonebook[name] = number  # Store name as key and number as value in the dictionary

# Handle queries: Read input until EOF (end of input)
for line in sys.stdin:
    query = line.strip()  # Remove leading/trailing spaces from the query
    if query in phonebook:  # Check if the query exists in the phonebook
        print(f"{query}={phonebook[query]}")  # If found, print the name and number in the format name=number
    else:
        print("Not found")  # If not found, print "Not found"
