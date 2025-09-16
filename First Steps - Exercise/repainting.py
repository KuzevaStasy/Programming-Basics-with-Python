square_meters_naylon = int(input())
paint_in_litres = int(input())
thinner_in_litres = int(input())
work_hours = int(input())
sum_bag = 0.40

sum_naylon = (square_meters_naylon +2) * 1.50
sum_paint = (paint_in_litres * 1.10) * 14.50
sum_thinner = thinner_in_litres * 5.00
total_sum_for_materials = sum_naylon + sum_paint + sum_thinner + sum_bag
sum_for_workers = (total_sum_for_materials * 0.30) * work_hours
total_sum = total_sum_for_materials + sum_for_workers

print(total_sum)