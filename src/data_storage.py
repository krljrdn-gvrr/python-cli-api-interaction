import json
import csv
import sqlite3

class DataStorage:
    def __init__(self, storage_format, storage_path):
        self.storage_format = storage_format
        self.storage_path = storage_path

    def save(self, data):
        if self.storage_format == "json":
            with open(self.storage_path, "w") as f:
                json.dump(data, f)
        elif self.storage_format == "csv":
            with open(self.storage_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        elif self.storage_format == "sqlite":
            with sqlite3.connect(self.storage_path) as conn:
                cursor = conn.cursor()
                table_name = "api_data"
                columns = ", ".join(data[0].keys())
                placeholders = ", ".join("?" for _ in data[0].keys())
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
                for row in data:
                    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", tuple(row.values()))
        else:
            raise ValueError(f"Unsupported storage format: {self.storage_format}")
