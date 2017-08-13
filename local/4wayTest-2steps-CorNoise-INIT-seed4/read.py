import csv

with open("Returns_seed4.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


