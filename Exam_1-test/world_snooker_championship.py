stage = input()
ticket_type = input()
ticket_count = int(input())
photo_option = input()

price_per_ticket = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price_per_ticket = 55.50
    elif ticket_type == "Premium":
        price_per_ticket = 105.20
    elif ticket_type == "VIP":
        price_per_ticket = 118.90

elif stage == "Semi final":
    if ticket_type == "Standard":
        price_per_ticket = 75.88
    elif ticket_type == "Premium":
        price_per_ticket = 125.22
    elif ticket_type == "VIP":
        price_per_ticket = 300.40

elif stage == "Final":
    if ticket_type == "Standard":
        price_per_ticket = 110.10
    elif ticket_type == "Premium":
        price_per_ticket = 160.66
    elif ticket_type == "VIP":
        price_per_ticket = 400.00

# total price without discount
total_price = price_per_ticket * ticket_count

# discount
if total_price > 4000:
    total_price *= 0.75  # 25% discount
    photo_option = 'N'  # free pictures
elif total_price > 2500:
    total_price *= 0.90  # 10% discount

# add picture if it not free
if photo_option == 'Y':
    total_price += ticket_count * 40

# print total price
print(f"{total_price:.2f}")
