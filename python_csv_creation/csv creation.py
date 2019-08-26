
import csv

names = []
jobs = []


with open('persons.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        # print(row.replace("\n", ""))
