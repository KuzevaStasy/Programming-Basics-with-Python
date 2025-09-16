visitors = int(input())

back = 0
chest = 0
legs = 0
abs_ex = 0
protein_shake = 0
protein_bar = 0

for _ in range(visitors):
    activity = input()
    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs_ex += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

total_training = back + chest + legs + abs_ex
total_protein = protein_shake + protein_bar

percent_training = (total_training / visitors) * 100
percent_protein = (total_protein / visitors) * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_ex} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")
