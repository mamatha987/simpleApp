# List of student grades
grades = [85, 90, 78, 92, 88, 76, 95, 89]

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Write the result to a text file
with open("average_grade.txt", "w") as file:
    file.write(f"The average grade is: {average_grade:.2f}")

print("The average grade has been written to average_grade.txt")
