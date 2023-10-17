import random
import csv

min_num = 1
max_num = 9410

num_of_gen = 20

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as file:
    spisok = csv.reader(file, delimiter=';')

    text = []
    spisok_full = []

    for line in spisok:
        author = line[3]
        book_name = line[1]
        year = line[6][6:10]
        spisok_full.append(f'{author} - "{book_name}" - {year}')

    for row in range(num_of_gen):
        gen = random.randint(min_num, max_num)
        text.append(spisok_full[gen])

with open('generation.txt', '+w', encoding="cp1251", errors="ignore") as file:
    num = 0
    for line in text:
        num += 1
        file.write(f'{num} {line};\n')

