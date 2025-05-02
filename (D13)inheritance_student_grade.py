# Base class: Person
class Person:
    # Constructor to initialize first name, last name, and ID
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    # Method to print person's full name and ID
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

# Derived class: Student (inherits from Person)
class Student(Person):
    # Constructor with scores added
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)  # Call parent constructor
        self.scores = scores

    # Method to calculate grade based on average score
    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        if average >= 90:
            return 'O'  # Outstanding
        elif average >= 80:
            return 'E'  # Exceeds Expectations
        elif average >= 70:
            return 'A'  # Acceptable
        elif average >= 55:
            return 'P'  # Poor
        elif average >= 40:
            return 'D'  # Dreadful
        else:
            return 'T'  # Troll

# Read input for first name, last name, and ID
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]

# Read number of scores (not needed in Python, kept for compatibility)
numScores = int(input())

# Read the actual scores as a list of integers
scores = list(map(int, input().split()))

# Create Student object
s = Student(firstName, lastName, idNum, scores)

# Print personal details
s.printPerson()

# Print grade based on average score
print("Grade:", s.calculate())
