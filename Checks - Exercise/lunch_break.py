import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
relax_time = break_duration / 4

time_left = break_duration - lunch_time - relax_time

if time_left >= episode_duration:
    free_time = math.ceil(time_left - episode_duration)
    print(f"You have enough time to watch {series_name} and left with {free_time} minutes free time.")
else:
    needed_time = math.ceil(episode_duration - time_left)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")