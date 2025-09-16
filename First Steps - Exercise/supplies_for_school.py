count_pakage_pens = int(input())
count_pakage_markers = int(input())
cleaning_litres = int(input())
discount_percent = int(input())

pens_sum = count_pakage_pens * 5.80
markers_sum = count_pakage_markers * 7.20
sum_cleaning = cleaning_litres * 1.20
all_sum = pens_sum + markers_sum + sum_cleaning
sum_discount = all_sum - (all_sum * (discount_percent / 100))

print(sum_discount)