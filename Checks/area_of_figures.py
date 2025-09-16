import math

# Четене на вида на фигурата
figure_type = input("Въведете вида на фигурата (square, rectangle, circle, triangle): ")

# Пресмятане на лицето според вида
if figure_type == "square":
    side = float(input("Въведете дължина на страната: "))
    area = side * side

elif figure_type == "rectangle":
    side1 = float(input("Въведете първата страна: "))
    side2 = float(input("Въведете втората страна: "))
    area = side1 * side2

elif figure_type == "circle":
    radius = float(input("Въведете радиус: "))
    area = math.pi * radius * radius

elif figure_type == "triangle":
    base = float(input("Въведете основа: "))
    height = float(input("Въведете височина към основата: "))
    area = (base * height) / 2

else:
    print("Невалиден вид фигура!")
    area = None

# Отпечатване на резултата, ако има изчислена площ
if area is not None:
    print(f"Лицето е: {area:.3f}")