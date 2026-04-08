import csv

class CSVValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.errors = []
        self.data = []
        self.columns = []

    def load(self):
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.columns = [col.strip().lower() for col in reader.fieldnames]
                self.data = list(reader)
        except FileNotFoundError:
            self.errors.append("File not found")
        except Exception as e:
            self.errors.append(str(e))

    def validate_schema(self, expected_columns, strict=True):
        expected = [col.strip().lower() for col in expected_columns]

        if strict:
            if self.columns != expected:
                self.errors.append(f"Schema mismatch: {self.columns}")
        else:
            # allow extra columns
            if not set(expected).issubset(set(self.columns)):
                self.errors.append(f"Missing required columns: {expected}")

    def validate_row_count(self, min_rows=1):
        if len(self.data) < min_rows:
            self.errors.append(
                f"Not enough rows: found {len(self.data)}, expected {min_rows}"
            )

    def validate_no_nulls(self):
        for i, row in enumerate(self.data, start=1):
            for key, value in row.items():
                if value is None or value.strip() == "":
                    self.errors.append(f"Null value at row {i}, column '{key}'")

    def result(self):
        return {
            "is_valid": len(self.errors) == 0,
            "errors": self.errors
        }