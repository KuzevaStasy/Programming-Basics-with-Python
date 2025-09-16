age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toys_count = 0
gift_money = 10

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money += gift_money - 1
        gift_money += 10
    else:
        toys_count += 1

money += toys_count * toy_price

if money >= washing_machine_price:
    print(f"Yes! {money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money:.2f}")
