poor_grades_limit = int(input())

poor_grades = 0
total_score = 0
problems_count = 0
last_problem = ""

while True:
    problem_name = input()
    if problem_name == "Enough":
        average_score = total_score / problems_count
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problems_count}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())
    total_score += grade
    problems_count += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades += 1
        if poor_grades == poor_grades_limit:
            print(f"You need a break, {poor_grades} poor grades.")
            break
