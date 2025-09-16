budget = float(input())
season = input()

destination = ""
place_type = ""
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = budget * 0.30
        place_type = "Camp"
    else:  # winter
        spent = budget * 0.70
        place_type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = budget * 0.40
        place_type = "Camp"
    else:  # winter
        spent = budget * 0.80
        place_type = "Hotel"
else:
    destination = "Europe"
    spent = budget * 0.90
    place_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_type} - {spent:.2f}")
