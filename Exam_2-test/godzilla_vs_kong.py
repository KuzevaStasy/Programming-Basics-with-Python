film_budget = float(input())
count_stat = int(input())
dress_for_one_stat = float(input())

decor = film_budget * 0.10

if count_stat > 150:
    price_for_dress = count_stat * dress_for_one_stat
    discount = price_for_dress * 0.1
    total_price_for_dress = price_for_dress - discount
else:
    total_price_for_dress = count_stat * dress_for_one_stat

total_price_for_film = total_price_for_dress + decor

if total_price_for_film > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price_for_film - film_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_price_for_film:.2f} leva left.")