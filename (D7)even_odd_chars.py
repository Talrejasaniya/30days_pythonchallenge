# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read the number of test cases
T = int(input())

# Loop over each test case
for _ in range(T):
    s = input()  # Read the input string for this test case

    even_chars = ""  # To store characters at even indices
    odd_chars = ""   # To store characters at odd indices

    # Iterate through the string using index
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]  # Add even-indexed character
        else:
            odd_chars += s[i]   # Add odd-indexed character

    # Print even and odd characters separated by a space
    print(even_chars + " " + odd_chars)
