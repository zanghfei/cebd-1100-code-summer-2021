# Get full items
# for key, value in my_dict.items()
#    print(key, value)
# Combine both
# for key in my_dict
#    print(my_dict[key])


provinces = {"QC": "Quebec", "ON": "Ontario", "PQ": "Quebec"}

for x in provinces.items():
    print(x[0] + "   " + x[1])

for v in provinces.values():
    print(v)

for k in provinces.keys():
    print(k)

print("ON" in provinces)
