egg_count = int(input())

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0

for _ in range(egg_count):
    color = input()
    if color == "red":
        red_count += 1
    elif color == "orange":
        orange_count += 1
    elif color == "blue":
        blue_count += 1
    elif color == "green":
        green_count += 1

max_eggs = red_count
max_color = "red"

if orange_count > max_eggs:
    max_eggs = orange_count
    max_color = "orange"
if blue_count > max_eggs:
    max_eggs = blue_count
    max_color = "blue"
if green_count > max_eggs:
    max_eggs = green_count
    max_color = "green"

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_eggs} -> {max_color}")
