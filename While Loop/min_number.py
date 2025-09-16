min_number = None

while True:
    command = input()

    if command == "Stop":
        break

    number = int(command)

    if min_number is None or number < min_number:
        min_number = number

print(f"{min_number}")
