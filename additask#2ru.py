import csv

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as file:
    file_reader = csv.reader(file, delimiter=';')
    result = (sorted(file_reader, reverse=True,  key=lambda file_reader: file_reader[8]))[1:21]

    num = 0

    for line in result:
        num += 1
        author = line[3]
        book_name = line[1]
        given = line[8]
        print(f'{num} - Автор: {author} - Название книги: {book_name} - Кол-во выдач: {given}')
