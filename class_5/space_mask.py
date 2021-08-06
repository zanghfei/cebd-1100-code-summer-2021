phrase = "THIS IS A PHRASE"

chosen = "A"

for x in phrase:
    if x in chosen or x == " ":
        print(x, end=" ")
    else:
        print("_", end=" ")
