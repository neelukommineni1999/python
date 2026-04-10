# This program checks whether incoming data is valid, complete, and usable.

name = input("Enter name: ")
age = int(input("Enter age: "))
price = float(input("Enter price: "))
email = input("Enter email: ")


if name == "" or email == "":
    print("Error: Required fields are missing")

# Check age condition
elif age < 0:
    print("Error: Invalid age")

elif age > 18:
    print("User is an adult")

else:
    print("User is a minor")

# Check price condition
if price > 100:
    print("Price is expensive")

elif price > 0:
    print("Price is affordable")

else:
    print("Error: Invalid price")

# Email validation
if "@" in email:
    print("Valid email format")
else:
    print("Invalid email format")
