fat_in_percent = float(input())
protein_in_percent = float(input())
carbohydrates_in_percent = float(input())
count_calories = int(input())
body_water_procent = float(input())

fat_in_grams = (count_calories * fat_in_percent / 100) / 9
protein_in_grams = (count_calories * protein_in_percent / 100) / 4
carbohydrates_in_grams = (count_calories * carbohydrates_in_percent / 100) / 4
foot_in_grams = fat_in_grams + protein_in_grams + carbohydrates_in_grams
calories_in_one_gram_foot = count_calories / foot_in_grams
water = (100 - body_water_procent) / 100
total_calories = water * calories_in_one_gram_foot

print(f"{total_calories:.4f}")