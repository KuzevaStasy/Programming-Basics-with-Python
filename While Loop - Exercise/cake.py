wight = int(input())
lenght = int(input())

total_pies = wight * lenght

given_pies = 0

while given_pies < total_pies:
    enter = input()
    if enter == "STOP":
        break
    pies = int(enter)
    given_pies += pies

diff = total_pies - given_pies

if diff >= 0:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {abs(diff)} pieces more.")
