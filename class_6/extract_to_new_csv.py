import csv

fi = open("csv_files\\7 - 100 Sales Records.csv", 'rt')
fo = open("csv_files\\filtered.csv", 'w', newline="")

reader = csv.reader(fi)
writer = csv.writer(fo, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    temp_list = []
    temp_list.append(row[0])
    temp_list.append(row[1])
    temp_list.append(row[8])
    writer.writerow(temp_list)
