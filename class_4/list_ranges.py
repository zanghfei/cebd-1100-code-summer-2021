my_list = ["A", "B", "C", "D", "E"]

# sublist = my_list[-2:]
#
# print(sublist)

my_list.append("F")

print(my_list)

my_list = my_list + ["X", "Y"]

print(my_list)

my_ranged_list = list(range(1, 11))

my_inefficient_list = []

for num in range(1, 11):
    my_inefficient_list.append(num)

my_inefficient_list = []

