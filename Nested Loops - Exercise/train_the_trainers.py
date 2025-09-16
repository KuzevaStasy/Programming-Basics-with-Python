jury_count = int(input())

total_average_sum = 0
presentation_count = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    grades_sum = 0
    for _ in range(jury_count):
        grade = float(input())
        grades_sum += grade

    average = grades_sum / jury_count
    print(f"{presentation_name} - {average:.2f}.")

    total_average_sum += average
    presentation_count += 1

final_assessment = total_average_sum / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")
