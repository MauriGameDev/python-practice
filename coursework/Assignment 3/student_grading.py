"""Calculate the student's final grade
and validate each category."""

# named constants
EXAM_WEIGHT = 0.50
ASSIGNMENT_WEIGHT = 0.30
QUIZ_WEIGHT = 0.20

MAX_EXAM_GRADE = 100
MAX_ASSIGNMENT_GRADE = 30
MAX_QUIZ_GRADE = 20

# initialize category grades
exam_grade = 0
assignment_grade = 0
quiz_grade = 0

# get grades from the user
midterm_exam_grade = float(input('Please enter midterm grade 0 - 100: '))
final_exam_grade = float(input('Please enter final exam grade 0 - 100: '))

assignment_one = float(input('Please enter first assignment grade 0 - 30: '))
assignment_two = float(input('Please enter second assignment grade 0 - 30: '))

quiz_one = float(input('Please enter first quiz grade 0 - 20: '))
quiz_two = float(input('Please enter second quiz grade 0 - 20: '))

# validate and calculate exam grade
if (midterm_exam_grade >= 0 and midterm_exam_grade <= MAX_EXAM_GRADE
        and final_exam_grade >= 0 and final_exam_grade <= MAX_EXAM_GRADE):

    exam_average = (midterm_exam_grade + final_exam_grade) / 2
    exam_grade = exam_average * EXAM_WEIGHT

else:
    print('Invalid input. Please enter exams within the 0 - 100 range.')

# validate and calculate assignment grade
if (assignment_one >= 0 and assignment_one <= MAX_ASSIGNMENT_GRADE
        and assignment_two >= 0 and assignment_two <= MAX_ASSIGNMENT_GRADE):

    assignment_average = (assignment_one + assignment_two) / 2

    assignment_grade = (
        assignment_average / MAX_ASSIGNMENT_GRADE
    ) * 100 * ASSIGNMENT_WEIGHT

else:
    print('Invalid input. Please enter assignments within the 0 - 30 range.')

# validate and calculate quiz grade
if (quiz_one >= 0 and quiz_one <= MAX_QUIZ_GRADE
        and quiz_two >= 0 and quiz_two <= MAX_QUIZ_GRADE):

    quiz_average = (quiz_one + quiz_two) / 2

    quiz_grade = (
        quiz_average / MAX_QUIZ_GRADE
    ) * 100 * QUIZ_WEIGHT

else:
    print('Invalid input. Please enter quizzes within the 0 - 20 range.')

# calculate the final grade
final_grade = exam_grade + assignment_grade + quiz_grade

# display the final grade
print(f"The student's final grade is {final_grade:.2f}%")