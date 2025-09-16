favorite_book = input()
books_checked = 0

while True:
    book = input()

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break

    if book == favorite_book:
        print(f"You checked {books_checked} books and found it.")
        break

    books_checked += 1
