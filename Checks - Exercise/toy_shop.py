vacantion_price = float(input())
count_puzzels = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_kamions = int(input())

PUZZEL = 2.60
DOLL = 3
BEAR = 4.10
MINION = 8.20
KAMION = 2

count_toys = count_bears + count_minions + count_puzzels + count_dolls + count_kamions

price = ((count_puzzels * PUZZEL) + (count_dolls * DOLL) + (count_bears * BEAR)
         + (count_minions * MINION) + (count_kamions * KAMION)
         )
if count_toys >= 50:
    discount = price * 0.25
    price = price - discount

profit = price - price * 0.10

if vacantion_price <= profit:
    print(f"Yes! {profit - vacantion_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacantion_price - profit:.2f} lv needed.")