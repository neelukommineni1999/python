import csv
import json

def clean_header(header):
    return header.lower().replace(" ", "_")

def main():
    cleaned_data = []
    seen_ids = set()

    with open("products_raw.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            new_row = {}

            # Step 1: clean headers + Step 2: handle missing values
            for key, value in row.items():
                clean_key = clean_header(key)

                if value == "" or value is None:
                    if clean_key == "price":
                        value = 0
                    elif clean_key == "stock":
                        value = 0
                    else:
                        value = "unknown"

                new_row[clean_key] = value

            # Step 3: remove duplicates
            product_id = new_row["product_id"]

            if product_id in seen_ids:
                continue

            seen_ids.add(product_id)

            cleaned_data.append(new_row)

    # Step 4: write JSON
    with open("products_cleaned.json", "w") as f:
        json.dump(cleaned_data, f, indent=4)

if __name__ == "__main__":
    main()