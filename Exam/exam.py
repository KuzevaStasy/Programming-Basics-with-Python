count_students = int(input())

fail_count = 0
between_3_4 = 0
between_4_5 = 0
top_students = 0
total_grades = 0

for _ in range(count_students):
    grade = float(input())
    total_grades += grade

    if grade < 3.00:
        fail_count += 1
    elif grade < 4.00:
        between_3_4 += 1
    elif grade < 5.00:
        between_4_5 += 1
    else:
        top_students += 1

fail_percent = (fail_count / count_students) * 100
between_3_4_percent = (between_3_4 / count_students) * 100
between_4_5_percent = (between_4_5 / count_students) * 100
top_percent = (top_students / count_students) * 100
average = total_grades / count_students

print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_5_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_4_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average:.2f}")
