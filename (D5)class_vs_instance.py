class Person:
    # Constructor to initialize the person's age
    def __init__(self, initialAge):
        # If the input age is valid (non-negative), assign it
        if initialAge >= 0:
            self.age = initialAge
        else:
            # If the input age is invalid (negative), set age to 0 and print a warning
            print("Age is not valid, setting age to 0.")
            self.age = 0

    # Method to determine and print the age category
    def amIOld(self):
        if self.age < 13:
            print("You are young.")         # If age is less than 13
        elif 13 <= self.age < 18:
            print("You are a teenager.")    # If age is between 13 and 17
        else:
            print("You are old.")           # If age is 18 or above

    # Method to simulate the passage of one year
    def yearPasses(self):
        self.age += 1  # Increment age by 1

# -------- Main logic starts here --------

# Read number of test cases
t = int(input())  # First input: how many people to test

# Loop over each test case
for i in range(0, t):
    age = int(input())         # Read the initial age for this person
    p = Person(age)            # Create a new Person object
    p.amIOld()                 # Print current age category
    for j in range(0, 3):      # Simulate 3 years passing
        p.yearPasses()
    p.amIOld()                 # Print updated age category after 3 years
    print("")                  # Print a blank line between test cases
