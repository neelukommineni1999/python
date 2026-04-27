age_text = "abc"

try:
    age = int(age_text)
    print(age)
except ValueError:
    print("Invalid age")