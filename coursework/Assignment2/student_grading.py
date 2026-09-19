"""calculate the student's grade based on the scores from the input and
   the predefined weights for each category"""

# define the weights for each category
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

# get the scores from the user
midterm_exam_grade = float(input('Please enter midterm grade: '))
final_exam_grade = float(input('Please enter final exam grade: '))
assignment_one = float(input('Please enter first assignment grade: '))
assignment_two = float(input('Please enter second assignment grade: '))
quiz_one = float(input('Please enter first quiz grade: '))
quiz_two = float(input('Please enter second quiz grade: '))

# calculate the average for each category and multiply by its weight
exam_grade = ((midterm_exam_grade + final_exam_grade) / 2) * EXAM_WEIGHT
assignment_grade = ((assignment_one + assignment_two) / 2) * ASSIGNMENT_WEIGHT
quiz_grade = ((quiz_one + quiz_two) / 2) * QUIZ_WEIGHT

# calculate the final grade and convert it to a percentage
final_grade = (exam_grade + assignment_grade + quiz_grade) / 100

# print the final grade with 2 decimal places using f-string formatting
print(f"The student's final grade is {final_grade:.2%}")