n = int(input())

numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

total_sum = sum(numbers)
found = False

for num in numbers:
    if num == total_sum - num:
        print("Yes")
        print(f"Sum = {num}")
        found = True
        break

if not found:
    max_num = max(numbers)
    others_sum = total_sum - max_num
    diff = abs(max_num - others_sum)
    print("No")
    print(f"Diff = {diff}")
