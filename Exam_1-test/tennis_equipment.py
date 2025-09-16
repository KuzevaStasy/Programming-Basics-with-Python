from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_count = int(input())
snikers_count = int(input())

racket_price = tennis_racket_price * tennis_racket_count
snikers_price = (tennis_racket_price / 6) * snikers_count
other_equipment = (racket_price + snikers_price) * 0.20
total_price = racket_price + snikers_price + other_equipment
djokovic_price = floor(total_price / 8)
sponsor_price = ceil(total_price * 7/8)

print(f"Price to be paid by Djokovic {djokovic_price}")
print(f"Price to be paid by sponsors {sponsor_price}")