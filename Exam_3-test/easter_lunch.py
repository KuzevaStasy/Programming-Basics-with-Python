SWEET_BREAD = 3.20
EGGS = 4.35 # for 12 eggs
COOKIES_FOR_ONE_KILOGRAM = 5.40
PAINT_EGG = 0.15

sweet_bread = int(input())
egg_packet_count = int(input())
cookies_kg = int(input())

sweet_bread_price = sweet_bread * SWEET_BREAD
egg_price = (egg_packet_count * EGGS) + (egg_packet_count * 12 * PAINT_EGG)
cookies_price = cookies_kg * COOKIES_FOR_ONE_KILOGRAM

total_price = sweet_bread_price + cookies_price + egg_price

print(f"{total_price:.2f}")