# Practice 12: Check for missing names and invalid ages in a list of records
names = ["neelu", "sree", "", "Baby"]
ages = [25, 17, 30, -5]

for i in range(len(names)):
    name = names[i]
    age = ages[i]
    print("\nRow", i)

    if name == "":
        print("Missing name")

    elif age < 0:
        print("Invalid age")

    elif age < 18:
        print("Minor")

    else:
        print("Valid record")
