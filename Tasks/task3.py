def process_customers(data):
    headers = data[0]

    clean_data = []
    error_log = []

    for row in data[1:]:
        try:
            customer_id = row[0]
            name = row[1]
            age = row[2]
            city = row[3]

            # check missing values
            if name == "":
                raise ValueError(f"missing name (customer_id={customer_id})")

            if city == "":
                raise ValueError(f"missing city (customer_id={customer_id})")

            # risky conversion
            try:
                age = int(age)
            except:
                raise ValueError(f"invalid age '{row[2]}' (customer_id={customer_id})")

            # valid record
            clean_data.append({
                "customer_id": int(customer_id),
                "name": name,
                "age": age,
                "city": city
            })

        except ValueError as e:
            error_msg = str(e)

            # store in memory for later use
            error_log.append(error_msg)

            # print log
            print("LOG:", error_msg)

            # write to file immediately
            with open("errors.log", "a") as f:
                f.write(error_msg + "\n")

    return clean_data, error_log


# INPUT DATA
data = [
    ["customer_id", "name", "age", "city"],
    ["1", "Ravi", "15", "Hyderabad"],
    ["2", "Asha", "abc", "Chennai"],
    ["3", "", "16", "Bangalore"],
    ["4", "Imran", "15", ""]
]

clean_data, error_log = process_customers(data)

print("\nCLEAN DATA:")
print(clean_data)

print("\nERROR LOG (in memory):")
print(error_log)