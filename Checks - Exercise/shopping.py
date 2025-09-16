budget = float(input())
video_cards = int(input())
processors = int(input())
ram_modules = int(input())

VIDEO_CARD_PRICE = 250
total_video_card_price = video_cards * VIDEO_CARD_PRICE
processor_price = 0.35 * total_video_card_price
ram_price = 0.10 * total_video_card_price

total_price = total_video_card_price + (processors * processor_price) + (ram_modules * ram_price)

if video_cards > processors:
    total_price *= 0.85

if budget >= total_price:
    remaining = budget - total_price
    print(f"You have {remaining:.2f} leva left!")
else:
    needed = total_price - budget
    print(f"Not enough money! You need {needed:.2f} leva more!")