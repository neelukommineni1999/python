import csv
import json

input_file = r"C:\Users\Neeli\OneDrive\Desktop\python\data.csv"
output_file = r"C:\Users\Neeli\OneDrive\Desktop\python\clean_data.json"

cleaned_data = []

with open(input_file, mode="r", newline="", encoding="utf-8") as csv_file:  
    reader = csv.DictReader(csv_file)

    # Standardize headers: lowercase + strip spaces
    reader.fieldnames = [field.strip().lower().replace(" ", "_") for field in reader.fieldnames]

    for row in reader:
        cleaned_row = {}

        for key, value in row.items():
            clean_key = key.strip().lower().replace(" ", "_")

            # Handle nulls
            if value is None or value.strip() == "":
                cleaned_row[clean_key] = None
            else:
                cleaned_row[clean_key] = value.strip()

        cleaned_data.append(cleaned_row)

# Write to JSON
with open(output_file, mode="w", encoding="utf-8") as json_file:
    json.dump(cleaned_data, json_file, indent=4)

print("✅ CSV cleaned and converted to JSON!")

from validator import CSVValidator

file_path = r"C:\Users\Neeli\OneDrive\Desktop\python\data.csv"

validator = CSVValidator(file_path)

validator.load()
validator.validate_schema(["name", "age", "email"], strict=False)
validator.validate_row_count(min_rows=2)
validator.validate_no_nulls()

result = validator.result()

if not result["is_valid"]:
    print("❌ Validation Failed:")
    for err in result["errors"]:
        print("-", err)
    exit()

print("✅ Validation Passed")