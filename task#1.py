allsum = 0

with open('lab1-main/books.csv', 'r', encoding="cp1251", errors="ignore") as file:
    for line in file:
        allsum += 1
    print(f'Количество записей в файле: {allsum}')

