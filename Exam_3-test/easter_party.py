count_guests = int(input())
price_for_one_guest = float(input())
budget = float(input())

cake_price = budget * 0.10

if count_guests < 10:
    price_for_one_guest = price_for_one_guest
elif 10 <= count_guests <= 15:
    price_for_one_guest = price_for_one_guest * 0.85
elif 15 < count_guests <= 20:
    price_for_one_guest = price_for_one_guest * 0.80
elif  count_guests > 20:
    price_for_one_guest = price_for_one_guest * 0.75

total_price = count_guests * price_for_one_guest + cake_price

if total_price <= budget:
    print(f"It is party time! {budget - total_price:.2f} leva left.")
else:
    print(f"No party! {total_price - budget:.2f} leva needed.")