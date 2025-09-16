n = int(input())
number = int(input())

max_value = number
min_value = number

for n in range(2, n + 1):
    number = int(input())
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")