flower_type = input()
flower_count = int(input())
budget = int(input())

prices = {
    "Roses": 5.00,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3.00,
    "Gladiolus": 2.50
}

price_per_flower = prices[flower_type]
total_price = flower_count * price_per_flower

if flower_type == "Roses" and flower_count > 80:
    total_price *= 0.90
elif flower_type == "Dahlias" and flower_count > 90:
    total_price *= 0.85
elif flower_type == "Tulips" and flower_count > 80:
    total_price *= 0.85
elif flower_type == "Narcissus" and flower_count < 120:
    total_price *= 1.15
elif flower_type == "Gladiolus" and flower_count < 80:
    total_price *= 1.20

difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
