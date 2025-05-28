import math  # Importing math module to use the square root function

# Take number of test cases as input
T = int(input())

# Loop through each test case
for _ in range(T):
    n = int(input())  # Read the number to check
    
    # Prime numbers are greater than 1
    if n <= 1:
        print("Not prime")
    else:
        is_prime = True  # Assume the number is prime

        # Check divisibility from 2 up to square root of n
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:  # If n is divisible by j, it's not a prime
                print("Not prime")
                is_prime = False
                break  # No need to check further

        # If no divisors were found, it is prime
        if is_prime:
            print("prime")
