import csv

allsum = 0
MAX_NAME = 30

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as file:
    file_reader = csv.reader(file, delimiter=';')

    for line in file_reader:
        if len(line[1]) > MAX_NAME:
            allsum += 1
    print(f'Количество записей, у которых поле "Название" строка длиннее 30 символов: {allsum}')