budget = float(input())
number_of_extras = int(input())
price_dress_for_onr_extra = float(input())

price_for_decor = budget * 0.10
price_for_dresses = number_of_extras * price_dress_for_onr_extra

if number_of_extras >= 150:
    discount = price_for_dresses * 0.10
    price_for_dresses = price_for_dresses - discount
else:
    price_for_dresses = number_of_extras * price_dress_for_onr_extra

total_price = price_for_decor + price_for_dresses

if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")