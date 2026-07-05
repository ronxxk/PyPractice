import random
import pandas

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(students_scores)
print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

# #Loop through a data frame
# for (key, value) in student_data_frame.items():
#   print(value)
#Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
I