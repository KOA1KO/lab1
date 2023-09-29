import csv
c = 0

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as f:
    fr = csv.reader(f, delimiter=';')

    for line in fr:
        if len(line[1]) > 30:
            c += 1
    print('Количество записей, у которых поле "Название" строка длиннее 30 символов: ' + str(c))