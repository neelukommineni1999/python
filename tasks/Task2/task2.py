def validate_dataset(data, expected_columns):
    # Step 1: get actual columns from first row
    actual_columns = data[0]

    # Step 2: compare expected vs actual
    missing_columns = [col for col in expected_columns if col not in actual_columns]
    extra_columns = [col for col in actual_columns if col not in expected_columns]

    schema_valid = len(missing_columns) == 0

    # Step 3: count rows (excluding header)
    total_rows = len(data) - 1

    # Step 4: classify rows as valid/invalid
    # If schema is broken, we consider all rows invalid
    if not schema_valid:
        valid_rows = 0
        invalid_rows = total_rows
    else:
        valid_rows = 0
        invalid_rows = 0

        # check each row for missing values
        for row in data[1:]:
            if len(row) == len(actual_columns) and all(value != "" for value in row):
                valid_rows += 1
            else:
                invalid_rows += 1

    # Step 5: return result dictionary
    return {
        "schema_valid": schema_valid,
        "missing_columns": missing_columns,
        "extra_columns": extra_columns,
        "total_rows": total_rows,
        "valid_rows": valid_rows,
        "invalid_rows": invalid_rows
    }



# Example usage

expected_columns = ["product_id", "product_name", "category", "price", "stock"]

data = [
    ["product_id","product_name","category","price"],
    ["201","Pen","Stationery","20"],
    ["202","Pencil","Stationery","10"]
]

result = validate_dataset(data, expected_columns)

print(result)