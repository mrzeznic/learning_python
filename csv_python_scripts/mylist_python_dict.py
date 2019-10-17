import csv
f = open("mylist.csv", 'rt')
try:
    reader = csv.DictReader(f)

    print(f"Columns in CSV file: {reader.fieldnames}")
    print(f"Dialect used in CSV file: {reader.dialect}")
    print(f"Current line number in CSV file: {reader.line_num}")
    print("Moving the reader to next line with reader.next() {}".format(
        next(reader)))
    print("Reading line numer: {}".format(reader.line_num))
    for row in reader:
        print(row['first_name'], row['last_name'], row['email'])
finally:
    f.close()
