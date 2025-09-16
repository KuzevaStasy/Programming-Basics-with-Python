student_name = input()
current_grade = 1
failures = 0
total_grade_sum = 0
grades_count = 0

while current_grade <= 12:
    yearly_grade = float(input())

    if yearly_grade < 4.00:
        failures += 1
        if failures > 1:
            print(f"{student_name} has been excluded at {current_grade} grade")
            break
        continue

    total_grade_sum += yearly_grade
    grades_count += 1
    current_grade += 1

if current_grade > 12 and failures <= 1:
    average = total_grade_sum / grades_count
    print(f"{student_name} graduated. Average grade: {average:.2f}")
