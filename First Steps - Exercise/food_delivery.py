count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegetarian_menus = int(input())
transport = 2.50

sum_for_chicken_menus = count_chicken_menus * 10.35
sum_for_fish_menus = count_fish_menus * 12.40
sum_for_vegetarisn_menus = count_vegetarian_menus * 8.15
sum_for_menus = sum_for_chicken_menus + sum_for_fish_menus + sum_for_vegetarisn_menus
sum_for_desert = sum_for_menus * 0.20

total = round(sum_for_menus + sum_for_desert + transport, 2)

print(total)
