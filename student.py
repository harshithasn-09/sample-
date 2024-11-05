# List of student grades
grades = [85, 92, 78, 90, 88]

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Write the result to a text file
with open("average_grade.txt", "w") as file:
    file.write(f"The average grade is: {average_grade:.2f}\n")

# Optionally, print the result to the console
print(f"The average grade is: {average_grade:.2f}")
