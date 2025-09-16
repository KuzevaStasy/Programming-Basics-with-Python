needed_money = float(input())
available_money = float(input())

days = 0
spend_days = 0

while available_money < needed_money:
    action = input()
    amount = float(input())
    days += 1

    if action == "spend":
        available_money -= amount
        if available_money < 0:
            available_money = 0
        spend_days += 1
    elif action == "save":
        available_money += amount
        spend_days = 0

    if spend_days == 5:
        print("You can't save the money.")
        print(days)
        break

if available_money >= needed_money:
    print(f"You saved the money for {days} days.")
