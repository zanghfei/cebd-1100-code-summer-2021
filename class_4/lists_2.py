# mylist = []
#
# mylist.append("A")
# mylist.append("B")
# mylist.append("C")
# mylist.append("D")
#
# del mylist[-1]
#
# print(mylist)
#
# val = mylist.pop()
#
# print(val)

mylist = ["A", "B", "A", "A"]

for a in mylist:
    if a == "B":
        del a

print(mylist)
