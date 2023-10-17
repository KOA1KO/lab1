import csv

with open('lab1-main/books-en.csv', 'r', encoding="cp1251", errors="ignore") as file:
    file_reader = csv.reader(file, delimiter=';')
    result = (sorted(file_reader, reverse=True,  key=lambda file_reader: file_reader[5]))[1:21]

    num = 0

    for line in result:
        num += 1
        author = line[2]
        book_name = line[1]
        downloads = line[5]
        print(f'{num} - Author: {author} - Name of book: {book_name} - Downloads: {downloads}')
