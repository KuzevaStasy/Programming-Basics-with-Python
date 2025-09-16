start = int(input())
end = int(input())

for num in range(start, end + 1):
    num_str = str(num)
    odd_sum = 0
    even_sum = 0

    for i in range(6):  # 6 цифри, индексите от 0 до 5
        digit = int(num_str[i])
        if (i + 1) % 2 == 0:  # четна позиция (1-базирано)
            even_sum += digit
        else:  # нечетна позиция
            odd_sum += digit

    if even_sum == odd_sum:
        print(num, end=" ")
