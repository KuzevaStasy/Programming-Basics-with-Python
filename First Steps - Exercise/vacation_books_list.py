pages_count = int(input())
pages_for_hour = int(input())
count_days = int(input())

total_hours = pages_count / pages_for_hour
needed_hours = int(total_hours / count_days)

print(needed_hours)