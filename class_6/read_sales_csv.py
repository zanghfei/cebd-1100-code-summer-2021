import csv

f = open("csv_files\\7 - 100 Sales Records.csv", 'rt')

reader = csv.reader(f)

next(reader)

item_types = set({})
sales_records = []
europe_counter = 0
total_sold = 0

for row in reader:
    sales_records.append(row)

# Records from Europe?

for record in sales_records:
    if record[0] == "Europe":
        europe_counter += 1

    total_sold += int(record[8])

    item_types.add(record[2])

print("Total records which apply to europe {}".format(europe_counter))
print("Total sold {}".format(total_sold))
print("The distinct item types are listed as follows:")

item_types = list(item_types)
item_types.sort()

for i in item_types:
    print(i)
