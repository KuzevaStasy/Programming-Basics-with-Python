days = int(input())
room_type = input()
rating = input()

nights = days - 1

price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

total_price = nights * price_per_night

if room_type == "apartment":
    if days < 10:
        total_price *= 0.70  # 30% намаление
    elif 10 <= days <= 15:
        total_price *= 0.65  # 35% намаление
    else:  # days > 15
        total_price *= 0.50  # 50% намаление

elif room_type == "president apartment":
    if days < 10:
        total_price *= 0.90  # 10% намаление
    elif 10 <= days <= 15:
        total_price *= 0.85  # 15% намаление
    else:  # days > 15
        total_price *= 0.80  # 20% намаление

if rating == "positive":
    total_price *= 1.25  # добавя 25%
else:  # negative
    total_price *= 0.90  # приспада 10%

print(f"{total_price:.2f}")
