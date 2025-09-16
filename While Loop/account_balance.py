total = 0.0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    amount = float(command)

    if amount < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    total += amount

print(f"Total: {total:.2f}")
