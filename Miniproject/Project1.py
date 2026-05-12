import csv

# READ CSV FILES
def read_csv(file_path):
    with open(file_path, "r") as f:
        return list(csv.reader(f))


vendor1 = read_csv("vendor1.csv")
vendor2 = read_csv("vendor2.csv")
vendor3 = read_csv("vendor3.csv")


# STANDARDIZE FUNCTION
def standardize_row(row, headers):
    mapping = {}

    for i in range(len(headers)):
        mapping[headers[i]] = row[i]

    return {
        "product_id": mapping.get("Product ID") or mapping.get("id") or mapping.get("item_code"),
        "product_name": mapping.get("Product Name") or mapping.get("name") or mapping.get("item_name"),
        "category": mapping.get("Category") or mapping.get("category") or mapping.get("item_group"),
        "price": mapping.get("Price") or mapping.get("price") or mapping.get("cost")
    }


# MAIN PROCESSING LOGIC
def process_vendor_data(vendors):
    clean_data = []
    invalid_data = []
    error_log = []
    seen_ids = set()

    for vendor in vendors:
        headers = vendor[0]

        for row in vendor[1:]:
            try:
                record = standardize_row(row, headers)

                product_id = record["product_id"]
                name = record["product_name"]
                category = record["category"]
                price = record["price"] or "0"

                # VALIDATION
                if not product_id or not name or not category:
                    raise ValueError(f"Missing required fields for product_id={product_id}")

                # convert price
                try:
                    price = int(price)
                except:
                    raise ValueError(f"Invalid price for product_id={product_id}")

                # duplicate check
                if product_id in seen_ids:
                    raise ValueError(f"Duplicate detected for product_id={product_id}")

                seen_ids.add(product_id)

                clean_data.append({
                    "product_id": product_id,
                    "product_name": name,
                    "category": category,
                    "price": price
                })

            except ValueError as e:
                error_log.append(str(e))
                invalid_data.append({
                    "row": row,
                    "error": str(e)
                })
                print("LOG:", e)

    return clean_data, invalid_data, error_log


# RUN PIPELINE
all_vendors = [vendor1, vendor2, vendor3]

clean_data, invalid_data, error_log = process_vendor_data(all_vendors)


# WRITE CLEAN DATA
with open("clean_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["product_id", "product_name", "category", "price"])
    writer.writeheader()
    writer.writerows(clean_data)


# WRITE BAD RECORDS
with open("bad_records.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["row", "error"])

    for item in invalid_data:
        writer.writerow([" | ".join(item["row"]), item["error"]])


# WRITE ERROR LOG
with open("error.log1", "w") as f:
    for err in error_log:
        f.write(err + "\n")


# FINAL SUMMARY
print("\nPIPELINE COMPLETED")
print("Clean Records:", len(clean_data))
print("Bad Records:", len(invalid_data))