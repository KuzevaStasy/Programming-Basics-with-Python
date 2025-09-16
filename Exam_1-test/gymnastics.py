country = input()
gymnastic_apparatus = input()

if country == "Russia":
    if gymnastic_apparatus == "ribbon":
        difficulty = 9.1
        performance = 9.4
        total_points = difficulty + performance
    elif gymnastic_apparatus == "hoop":
        difficulty = 9.3
        performance = 9.8
        total_points = difficulty + performance
    elif gymnastic_apparatus == "rope":
        difficulty = 9.6
        performance = 9.0
        total_points = difficulty + performance

if country == "Bulgaria":
    if gymnastic_apparatus == "ribbon":
        difficulty = 9.6
        performance = 9.4
        total_points = difficulty + performance
    elif gymnastic_apparatus == "hoop":
        difficulty = 9.55
        performance = 9.75
        total_points = difficulty + performance
    elif gymnastic_apparatus == "rope":
        difficulty = 9.5
        performance = 9.4
        total_points = difficulty + performance

if country == "Italy":
    if gymnastic_apparatus == "ribbon":
        difficulty = 9.2
        performance = 9.5
        total_points = difficulty + performance
    elif gymnastic_apparatus == "hoop":
        difficulty = 9.45
        performance = 9.35
        total_points = difficulty + performance
    elif gymnastic_apparatus == "rope":
        difficulty = 9.7
        performance = 9.15
        total_points = difficulty + performance

diff = 20 - total_points
percent = (diff / 20) * 100

print(f"The team of {country} get {total_points:.3f} on {gymnastic_apparatus}.")
print(f"{percent:.2f}%")