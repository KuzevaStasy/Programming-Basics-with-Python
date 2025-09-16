num_movies = int(input())

highest_rating = float('-inf')
lowest_rating = float('inf')
highest_movie = ''
lowest_movie = ''
total_rating = 0

for _ in range(num_movies):
    movie_name = input()
    rating = float(input())

    total_rating += rating

    if rating > highest_rating:
        highest_rating = rating
        highest_movie = movie_name

    if rating < lowest_rating:
        lowest_rating = rating
        lowest_movie = movie_name

average_rating = total_rating / num_movies

print(f"{highest_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
