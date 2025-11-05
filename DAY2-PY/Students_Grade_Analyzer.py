# 1. Data Representation and 2. Data Input:
student_grades = {
    "Alice": [88, 92, 78],
    "Bob": [75, 80, 85],
    "Charlie": [95, 89, 90]
}

# Dictionary to store the calculated averages
student_averages = {}

print("Student Grades and Averages:")

# 3. Iteration and Calculation:
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    student_averages[student] = average
    # 5. Output: Print the results in a readable format
    print(f"- {student}: Grades {grades}, Average: {average:.2f}")

print("\nSummary of Scores:")

# 4. Finding Max/Min:
# Find the highest and lowest scores among all students
all_grades = [grade for grades in student_grades.values() for grade in grades]

highest_score = max(all_grades)
lowest_score = min(all_grades)

# Find the student with the highest average grade
highest_average = max(student_averages, key=student_averages.get)

# Find the student with the lowest average grade
lowest_average = min(student_averages, key=student_averages.get)


# 5. Output: Print the results in a readable format
print(f"Highest individual score: {highest_score}")
print(f"Lowest individual score: {lowest_score}")
print(f"Student with the highest average: {highest_average} ({student_averages[highest_average]:.2f})")
print(f"Student with the lowest average: {lowest_average} ({student_averages[lowest_average]:.2f})")