import csv

f = open("csv_files\\7 - 100 Sales Records.csv", 'rt')

reader = csv.reader(f)

next(reader)

for row in reader:
    print(row)
