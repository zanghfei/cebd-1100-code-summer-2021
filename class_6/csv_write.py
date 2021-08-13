import csv

data = [["1",2,3], ["4",5,6], ["7",8,9]]



with open("example2.csv", "w", newline="") as c:
    writer = csv.writer(c, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)

