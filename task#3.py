import csv

lim_year = 16

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as file:
    file_reader = csv.reader(file, delimiter=';')

    findit = input('Введите имя, фамилию или отчество автора, чтобы я смог найти его книги, поступившие к нам до 2016 '
                   'года:')

    next(file_reader)
    for line in file_reader:
        author = line[4]
        year = int(line[6][8:10])
        if findit.lower() in author.lower() and year < lim_year:
            book_name = line[1]
            print(f'Автор: {author} - Название книги: {book_name}')