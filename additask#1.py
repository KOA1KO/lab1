import csv

with open('lab1-main/books-en.csv') as f:
    fr = csv.reader(f, delimiter=';')

    c = 0
    all_pub = []

    for line in fr:
        c += 1
        if c == 1:
            continue
        elif line[4].lower() not in str(all_pub).lower():
            all_pub.append(line[4])

    for i in all_pub:
        print(i)
