money_day = float(input())
sales_money_for_day = float(input())
expense_for_all_days = float(input())
price_for_gift = float(input())

save_money = 5 * money_day
earning_money = 5 * sales_money_for_day
total_save_money = save_money + earning_money
expenses = total_save_money - expense_for_all_days

if expenses > price_for_gift:
    print(f"Profit: {expenses:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {price_for_gift - expenses:.2f} BGN.")