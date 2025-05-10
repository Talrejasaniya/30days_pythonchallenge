# Define an interface-like base class
class AdvancedArithmetic(object):
    # Abstract method (meant to be overridden)
    def divisorSum(n):
        raise NotImplementedError

# Create a class that implements the above interface
class Calculator(AdvancedArithmetic):
    # Override the divisorSum method
    def divisorSum(self, n):
        self.n = n
        s = 0
        # Loop to find all divisors of n and sum them
        for i in range(1, n + 1):
            if n % i == 0:
                s = s + i
        return s

# Read integer input from user
n = int(input())

# Create object of Calculator class
my_calculator = Calculator()

# Call the divisorSum method
s = my_calculator.divisorSum(n)

# Print the name of the superclass (AdvancedArithmetic)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)

# Print the result of divisor sum
print(s)
