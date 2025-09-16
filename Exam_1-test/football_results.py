result_first_game = input()
result_second_game = input()
result_third_game = input()

wins = 0
losses = 0
draws = 0

# first game
home = int(result_first_game[0])
guest = int(result_first_game[2])

if home > guest:
    wins += 1
elif home < guest:
    losses += 1
elif home == guest:
    draws += 1

# second game
home = int(result_second_game[0])
guest = int(result_second_game[2])

if home > guest:
    wins += 1
elif home < guest:
    losses += 1
elif home == guest:
    draws += 1

# third game
home = int(result_third_game[0])
guest = int(result_third_game[2])

if home > guest:
    wins += 1
elif home < guest:
    losses += 1
elif home == guest:
    draws += 1

# print results
print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")