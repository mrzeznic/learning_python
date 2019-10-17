import csv
fh = open("mylist.csv", 'rt')
try:
    reader = csv.reader(fh)
    print("Data from the CSV:", list(reader))
except Exception as e:
    print("Exception is:", e)
finally:
    fh.close()
