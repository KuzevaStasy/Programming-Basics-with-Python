#read players name
player1 = input()
player2 = input()

# read points
points1 = 0
points2 = 0

while True:
    command = input()
    if command == "End of game":
        # if have end of the game write points
        print(f"{player1} has {points1} points")
        print(f"{player2} has {points2} points")
        break

    # read cards
    card1 = int(command)
    card2 = int(input())

    if card1 > card2:
        points1 += card1 - card2
    elif card2 > card1:
        points2 += card2 - card1
    else:
        # Number wars!
        print("Number wars!")
        # read two new cards
        card1 = int(input())
        card2 = int(input())

        if card1 > card2:
            print(f"{player1} is winner with {points1} points")
        else:
            print(f"{player2} is winner with {points2} points")
        break
