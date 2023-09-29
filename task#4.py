import random
import csv

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as f:
    spisok = csv.reader(f, delimiter=';')

    text = []
    spisok_full = []

    for y in spisok:
        spisok_full.append(y[3] + '. "' + y[1] + '" - ' + y[6][6] + y[6][7] + y[6][8] + y[6][9])

    for i in range(20):
        gen = random.randint(1, 9410)
        text.append(spisok_full[gen])

with open('generation.txt', '+w', encoding="cp1251", errors="ignore") as file:
    num = 0
    for u in text:
        num += 1
        file.write(str(num) + ' ' + u + ';\n')

