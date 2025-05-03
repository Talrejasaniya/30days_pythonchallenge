class Difference:
    def __init__(self, a):
        # Store the input list in a private instance variable
        self.__elements = a
        # Initialize maximumDifference to 0
        self.maximumDifference = 0

    def computeDifference(self):
        # Compute the maximum absolute difference between any two elements
        # This is simply the difference between the largest and smallest values
        self.maximumDifference = max(self.__elements) - min(self.__elements)

# ---------- Main Execution Part ----------

# Read the number of elements (not used, but commonly part of input)
_ = input()

# Read the array of integers from input
a = [int(e) for e in input().split(' ')]

# Create a Difference object with the array
d = Difference(a)

# Call method to compute the maximum difference
d.computeDifference()

# Print the result
print(d.maximumDifference)
