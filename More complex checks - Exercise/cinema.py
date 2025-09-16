projection_type = input()
r = int(input())
c = int(input())

seats = r * c

if projection_type == "Premiere":
    price = 12.00
elif projection_type == "Normal":
    price = 7.50
elif projection_type == "Discount":
    price = 5.00

total_income = seats * price

print(f"{total_income:.2f} leva")
