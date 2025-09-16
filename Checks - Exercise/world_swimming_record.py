import math

record_seconds = float(input())
distance_meters = float(input())
time_per_meter = float(input())

ivan_time = distance_meters * time_per_meter

delay_count = math.floor(distance_meters / 15)
total_delay = delay_count * 12.5

total_ivan_time = ivan_time + total_delay

if total_ivan_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_ivan_time:.2f} seconds.")
else:
    difference = total_ivan_time - record_seconds
    print(f"No, he failed! He was {difference:.2f} seconds slower.")