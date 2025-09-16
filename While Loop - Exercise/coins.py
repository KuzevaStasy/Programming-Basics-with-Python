sums = float(input())

stotinki = round(sums * 100)

coins = [200, 100, 50, 20, 10, 5, 2, 1]

count_coins = 0

for coin in coins:
    while stotinki >= coin:
        stotinki -= coin
        count_coins += 1

print(f"{count_coins}")
