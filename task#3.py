import csv

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as f:
    fr = csv.reader(f, delimiter=';')

    c1 = 0
    c2 = 0

    findit = input('Введите имя, фамилию или отчество автора, чтобы я смог найти его книги, поступившие к нам до 2016 года:')

    for i in fr:
        c1 += 1

        if c1 == 1:
            continue
        elif findit.lower() in i[4].lower() and int(i[6][8] + i[6][9]) < 16:
            print(f'Автор: {i[4]} - Название книги: {i[1]}')