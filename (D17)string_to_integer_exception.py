# Read a string input from the user
S = input()

# Try converting the string to an integer
try:
    print(int(S))  # If conversion is successful, print the integer
except ValueError:
    print("Bad String")  # If conversion fails, print "Bad String"
