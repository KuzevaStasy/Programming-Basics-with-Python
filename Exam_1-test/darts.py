player_name = input()

points = 301

successful_shots = 0
unsuccessful_shots = 0

while True:
    command = input()

    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    sector = command
    score = int(input())

    if sector == "Single":
        current_points = score
    elif sector == "Double":
        current_points = score * 2
    elif sector == "Triple":
        current_points = score * 3
    else:
        continue

    if current_points > points:
        unsuccessful_shots += 1
    else:
        points -= current_points
        successful_shots += 1

        if points == 0:
            print(f"{player_name} won the leg with {successful_shots} shots.")
            break
