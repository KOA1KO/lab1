import csv

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as f:
    fr = csv.reader(f, delimiter=';')
    res = (sorted(fr, reverse=True,  key=lambda fr: fr[8]))[1:21]

    num = 0

    for i in res:
        num += 1
        print(str(num) + ' - Автор: ' + i[3] + ' - Название книги: ' + i[1] + ' - Кол-во выдач: ' + i[8])
