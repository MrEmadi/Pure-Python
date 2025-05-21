# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
"""
This is the scoring criteria:
- Scores 91 - 100: Grade = "Outstanding"
- Scores 81 - 90: Grade = "Exceeds Expectations"
- Scores 71 - 80: Grade = "Acceptable"
- Scores 70 or lower: Grade = "Fail"
"""
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def convert_to_grade(students: dict) -> dict:
    if len(students) == 0: return {}
    students_grades = {}
    for key in students:
        grade = "Fail" # 70 or lower
        if students[key] > 90: grade = "Outstanding" # 91 - 100
        elif students[key] > 80: grade = "Exceeds Expectations" # 81 - 90
        elif students[key] > 70: grade = "Acceptable" # 71 - 80
        students_grades[key] = grade
    return students_grades

print(convert_to_grade(student_scores))
