length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent = float(input())

volume_in_cm = length_in_cm * width_in_cm * height_in_cm
volume_in_litres = volume_in_cm / 1000
litres_in_tank = volume_in_litres * (1 - (percent / 100))

print(litres_in_tank)