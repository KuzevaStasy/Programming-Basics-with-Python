control_minutes = int(input())
control_seconds = int(input())
track_length = float(input())
seconds_per_100m = int(input())

# calculate time in seconds
control_total_seconds = control_minutes * 60 + control_seconds

# time without diff
marin_time = (track_length / 100) * seconds_per_100m

# calculate diff
discount = (track_length / 120) * 2.5

# total time
final_time = marin_time - discount

# comparison and print result
if final_time <= control_total_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {final_time:.3f}.")
else:
    diff = final_time - control_total_seconds
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
