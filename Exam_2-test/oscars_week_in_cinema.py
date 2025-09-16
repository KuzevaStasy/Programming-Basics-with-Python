film_name = input()
kind_room = input()
count_ticket = int(input())

if film_name == "A Star Is Born":
    if kind_room == "normal":
        total_price = count_ticket * 7.50
    elif kind_room == "luxury":
        total_price = count_ticket * 10.50
    elif kind_room == "ultra luxury":
        total_price = count_ticket * 13.50
elif film_name == "Bohemian Rhapsody":
    if kind_room == "normal":
        total_price = count_ticket * 7.35
    elif kind_room == "luxury":
        total_price = count_ticket * 9.45
    elif kind_room == "ultra luxury":
        total_price = count_ticket * 12.75
elif film_name == "Green Book":
    if kind_room == "normal":
        total_price = count_ticket * 8.15
    elif kind_room == "luxury":
        total_price = count_ticket * 10.25
    elif kind_room == "ultra luxury":
        total_price = count_ticket * 13.25
elif film_name == "The Favourite":
    if kind_room == "normal":
        total_price = count_ticket * 8.75
    elif kind_room == "luxury":
        total_price = count_ticket * 11.55
    elif kind_room == "ultra luxury":
        total_price = count_ticket * 13.95

print(f"{film_name} -> {total_price:.2f} lv.")