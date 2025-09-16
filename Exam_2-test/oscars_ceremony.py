rent_for_room = int(input())

statuets = rent_for_room * 0.7
ceturing = statuets * 0.85
music = ceturing / 2

total = rent_for_room + statuets + ceturing + music
print(f"{total:.2f}")