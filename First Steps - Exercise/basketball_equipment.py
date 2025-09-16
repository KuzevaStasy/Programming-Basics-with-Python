paid_for_year = int(input())

sneakers = paid_for_year - (paid_for_year * 0.40)
siut = sneakers - (sneakers * 0.20)
ball = siut / 4
accessories = ball / 5

total_sum_for_equpment = paid_for_year + sneakers + siut + ball + accessories

print(total_sum_for_equpment)