specific_book = input()
checked_books = 0
while True:
    book = input()
    if book == specific_book:
        print(f"You checked {checked_books} books and found it.")
        break
    if book == 'No More Books':
        print(f"The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    checked_books += 1
