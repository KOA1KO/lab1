import csv

with open('lab1-main/books-en.csv', 'r', encoding="cp1251", errors="ignore") as f:
    fr = csv.reader(f, delimiter=';')
    res = (sorted(fr, reverse=True,  key=lambda fr: fr[5]))[1:21]

    num = 0

    for i in res:
        num += 1
        print(str(num) + ' - Author: ' + i[2] + ' - Name of book: ' + i[1] + ' - Downloads: ' + i[5])
