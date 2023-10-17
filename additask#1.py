import csv

with open('lab1-main/books-en.csv') as file:
    file_reader = csv.reader(file, delimiter=';')

    all_pub = []

    next(file_reader)
    for line in file_reader:
        name = line[4]
        if name.lower() not in str(all_pub).lower():
            all_pub.append(name)

    for words in all_pub:
        print(words)
