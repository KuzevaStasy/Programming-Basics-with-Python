deposit_sum = float(input())
deposit_in_month = int(input())
interest_for_year = float(input())

interes_sum = deposit_sum * (interest_for_year / 100)
interest_sum_for_one_month = interes_sum / 12
total_sum = deposit_sum + (deposit_in_month * interest_sum_for_one_month)

print(total_sum)