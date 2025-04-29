# factorial_recursive.py

# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n - 1)
        return n * factorial(n - 1)

if __name__ == '__main__':
    # Take input from the user
    n = int(input("Enter a number to find its factorial: ").strip())
    
    # Calculate factorial using recursion
    result = factorial(n)

    # Print result to console
    print("Factorial:", result)

    # Write result to a file named output.txt
    with open('output.txt', 'w') as f:
        f.write(str(result) + '\n')
