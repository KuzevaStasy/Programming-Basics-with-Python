count_people = int(input())
kind_season = input()

if count_people <= 5:
    if kind_season == "spring":
        price = count_people * 50.00
    if kind_season == "summer":
        price = count_people * 48.50
        discount = price * 0.15
        price -= discount
    if kind_season == "autumn":
        price = count_people * 60.00
    if kind_season == "winter":
        price = count_people * 86.00
        price_increase = price * 0.08
        price += price_increase
elif count_people > 5:
    if kind_season == "spring":
        price = count_people * 48.00
    if kind_season == "summer":
        price = count_people * 45.00
        discount = price * 0.15
        price -= discount
    if kind_season == "autumn":
        price = count_people * 49.50
    if kind_season == "winter":
        price = count_people * 85.00
        price_increase = price * 0.08
        price += price_increase

print(f"{price:.2f} leva.")