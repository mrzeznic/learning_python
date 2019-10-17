import csv

names = ["John", "Eve", "Fate", "Jadon"]
grades = ["C", "A+", "A", "B-"]
f = open("newlist.csv", 'w', newline='')

try:
    writer = csv.writer(f)
    writer.writerow(('Sr.', 'Names', 'Grades'))
    for i in range(4):
        writer.writerow((i+1, names[i], grades[i]))
finally:
    f.close
