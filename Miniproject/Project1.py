import json

# Vendor Data

vendor1 = [
    ["Product ID", "Product Name", "Price", "Category"],
    ["1001", "Wireless Mouse", "799", "Electronics"],
    ["1002", "Office Chair", "4999", "Furniture"],
    ["1003", "Laptop Stand", "", "Electronics"]  # missing price
]

vendor2 = [
    ["id", "name", "category", "price"],
    ["1002", "Office Chair", "Furniture", "4999"],
    ["1004", "Desk Lamp", "Home", "1299"],
    ["1005", "Water Bottle", "Home", "299"]
]

vendor3 = [
    ["item_code", "item_name", "item_group", "cost"],
    ["1006", "Notebook", "Stationery", "49"],
    ["1007", "Pen", "Stationery", "20"],
    ["1001", "Wireless Mouse", "Electronics", "799"]
]

# Column Mapping (Standard Schema)


def standardize_row(row, headers):
    mapping = {}

    for i in range(len(headers)):
        mapping[headers[i]] = row[i]

    # Convert to standard schema
    return {
        "product_id": mapping.get("Product ID") or mapping.get("id") or mapping.get("item_code"),
        "product_name": mapping.get("Product Name") or mapping.get("name") or mapping.get("item_name"),
        "category": mapping.get("Category") or mapping.get("category") or mapping.get("item_group"),
        "price": mapping.get("Price") or mapping.get("price") or mapping.get("cost")
    }

# Main Processing Function

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
                price = record["price"]
                category = record["category"]
                
                # Validation Rules

                if not product_id or not name or not category:
                    raise ValueError(f"Missing required fields in product {product_id}")

                if price == "" or price is None:
                    raise ValueError(f"Missing price for product {product_id}")

                # Convert price
                try:
                    record["price"] = int(price)
                except:
                    raise ValueError(f"Invalid price for product {product_id}")

                # Duplicate check
                if product_id in seen_ids:
                    raise ValueError(f"Duplicate product_id {product_id}")

                seen_ids.add(product_id)

                # Add to clean data
                clean_data.append(record)

            except ValueError as e:
                error_log.append(str(e))
                invalid_data.append({"row": row, "error": str(e)})
                print("LOG:", e)

    return clean_data, invalid_data, error_log

# Run Pipeline

all_vendors = [vendor1, vendor2, vendor3]

clean_data, invalid_data, error_log = process_vendor_data(all_vendors)

# Output Results

print("\nCLEAN DATA:")
print(json.dumps(clean_data, indent=4))

print("\nINVALID DATA:")
print(json.dumps(invalid_data, indent=4))

print("\nERROR LOG:")
for err in error_log:
    print("-", err)