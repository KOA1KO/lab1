c = 0

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as f:
    for line in f:
        c += 1
    print('Количество записей в файле: ' + str(c))

