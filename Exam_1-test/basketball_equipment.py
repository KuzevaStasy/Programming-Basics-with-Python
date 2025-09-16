years_price = int(input())

snicker_price = years_price - (years_price * 0.40)
swuit = snicker_price - (snicker_price * 0.20)
ball = swuit / 4
accessories = ball / 5

total_price = snicker_price + swuit + ball + accessories + years_price

print(f"{total_price:.2f}")
