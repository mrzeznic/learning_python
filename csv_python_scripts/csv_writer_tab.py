import csv

f = open("write.csv", 'wt', newline='')
csvWriter = csv.writer(f, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['abc', 'pqr', 'xyz'])
csvWriter.writerow(['123', '456', '789'])
f.close()
