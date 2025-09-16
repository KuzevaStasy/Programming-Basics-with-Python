num_cakes = int(input())

best_baker = ""
max_points = 0

for _ in range(num_cakes):
    baker_name = input()
    total_points = 0

    while True:
        grade = input()
        if grade == "Stop":
            break
        total_points += int(grade)

    print(f"{baker_name} has {total_points} points.")

    if total_points > max_points:
        max_points = total_points
        best_baker = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{best_baker} won competition with {max_points} points!")
