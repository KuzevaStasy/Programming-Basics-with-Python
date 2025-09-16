current_height = 5364
days = 1

while True:
    command = input()
    if command == "END":
        break

    rest = command  # "Yes" or "No"
    meters = int(input())

    if rest == "Yes":
        days += 1

    if days > 5:
        break

    current_height += meters

    if current_height >= 8848:
        break

if current_height >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{current_height}")
