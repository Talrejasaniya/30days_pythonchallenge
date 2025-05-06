# Write your code here

# Define a Calculator class
class Calculator():
    # Constructor method (currently not used, but defined as a good practice)
    def __init__(self):
        pass

    # Method to calculate power with exception handling for negative inputs
    def power(self, n, p):
        # Raise an exception if either n or p is negative
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        # Return the result of n raised to the power of p
        return n ** p

# Create an object of Calculator
myCalculator = Calculator()

# Take number of test cases as input
T = int(input())

# Loop through each test case
for i in range(T):
    # Read two integers n and p
    n, p = map(int, input().split())
    try:
        # Call the power method and store the result
        ans = myCalculator.power(n, p)
        # Print the result
        print(ans)
    except Exception as e:
        # If an exception is raised, print the exception message
        print(e)
