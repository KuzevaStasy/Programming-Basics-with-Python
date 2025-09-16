width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height

occupied_volume = 0

while occupied_volume < total_volume:
    entrance = input()
    if entrance == "Done":
        break
    cartons = int(entrance)
    occupied_volume += cartons

diff = total_volume - occupied_volume

if diff >= 0:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(diff)} Cubic meters more.")
