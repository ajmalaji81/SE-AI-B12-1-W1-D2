# User to enter a mark
mark = float(input("Enter your mark (0-100): "))

# Check if the mark is valid
if mark < 0 or mark > 100:
    Grade = "Invalid mark"

elif mark >= 90:
    Grade = "A"

elif mark >= 80:
    Grade = "B"

elif mark >= 70:
    Grade = "C"

elif mark >= 60:
    Grade = "D"

else:
    Grade = "E"

# Print the mark and corresponding grade
print("Your mark is:", mark)
print("Your grade is:", Grade) 
