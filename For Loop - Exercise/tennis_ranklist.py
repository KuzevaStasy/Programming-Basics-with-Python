from math import floor

tournaments = int(input())
starting_points = int(input())

total_points_earned = 0
wins = 0

for _ in range(tournaments):
    result = input()
    if result == "W":
        total_points_earned += 2000
        wins += 1
    elif result == "F":
        total_points_earned += 1200
    elif result == "SF":
        total_points_earned += 720

final_points = starting_points + total_points_earned
average_points = floor(total_points_earned / tournaments)
win_percent = (wins / tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")
