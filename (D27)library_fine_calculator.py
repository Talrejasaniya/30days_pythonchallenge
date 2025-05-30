# Take the returned date input, remove leading/trailing spaces, and split it into day, month, and year as integers
ret = input("Enter returned date (DD MM YYYY): ").strip()
day, month, year = map(int, ret.split())

# Take the due date input, remove spaces, and split into day, month, and year as integers
due = input("Enter due date (DD MM YYYY): ").strip()
d1, m1, y1 = map(int, due.split())

# Calculate fine based on the given rules
if year > y1:
    # If the book is returned in a later year
    fine = 10000
elif year == y1 and month > m1:
    # If returned in the same year but a later month
    fine = 500 * (month - m1)
elif year == y1 and month == m1 and day > d1:
    # If returned in the same month and year but a later day
    fine = 15 * (day - d1)
else:
    # If returned on or before the due date
    fine = 0

# Print the calculated fine
print("Fine:", fine)
