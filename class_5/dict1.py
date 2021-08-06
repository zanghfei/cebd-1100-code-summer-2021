d = {"A": 123, "B": 234}

# print(d[1])

d2 = list(d.values())
print(d2[1])

#print(d["A"])
#print(d["X"])

print(d.get("A"))
print(d.get("X", "NOT FOUND"))

if d.get("ABC") == None:
    pass

d.update({"C": 999})
d.update({"A": 111})

d["XYZ"] = "Hello"


#("Y" in d) # Is the key "Y" in the dictionary called d.

d.pop("U", "Default")

if "Y" in d:
    del d["Y"]
else:
    print("No record to delete")

# --> Complexity analysis / Asymptotic analysis
#   O(n/2)
#[1, 2, 3, 4, 5, 6, 7]

# del d["Y"]


