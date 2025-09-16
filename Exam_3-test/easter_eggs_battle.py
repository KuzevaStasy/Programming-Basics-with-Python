eggs_player1 = int(input())
eggs_player2 = int(input())

while True:
    command = input()

    if command == "End":
        print(f"Player one has {eggs_player1} eggs left.")
        print(f"Player two has {eggs_player2} eggs left.")
        break

    if command == "one":
        eggs_player2 -= 1
    elif command == "two":
        eggs_player1 -= 1

    if eggs_player1 == 0:
        print(f"Player one is out of eggs. Player two has {eggs_player2} eggs left.")
        break
    elif eggs_player2 == 0:
        print(f"Player two is out of eggs. Player one has {eggs_player1} eggs left.")
        break
