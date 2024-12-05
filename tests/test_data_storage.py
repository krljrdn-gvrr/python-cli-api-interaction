import pytest
import json
import csv
import sqlite3
from src.data_storage import DataStorage
from unittest.mock import mock_open, patch, MagicMock

def test_save_json():
    data = [{"key": "value"}]
    storage = DataStorage(storage_format="json", storage_path="test.json")

    with patch("builtins.open", mock_open()) as mock_file:
        storage.save(data)
        mock_file.assert_called_once_with("test.json", "w")
        mock_file().write.assert_called_once_with(json.dumps(data))

def test_save_csv():
    data = [{"key1": "value1", "key2": "value2"}]
    storage = DataStorage(storage_format="csv", storage_path="test.csv")

    with patch("builtins.open", mock_open()) as mock_file:
        with patch("csv.DictWriter") as mock_writer_class:
            mock_writer = MagicMock()
            mock_writer_class.return_value = mock_writer

            storage.save(data)

            mock_writer_class.assert_called_once_with(mock_file(), fieldnames=["key1", "key2"])
            mock_writer.writeheader.assert_called_once()
            mock_writer.writerows.assert_called_once_with(data)

def test_save_sqlite():
    data = [{"key1": "value1", "key2": "value2"}]
    storage = DataStorage(storage_format="sqlite", storage_path="test.db")

    with patch("sqlite3.connect") as mock_connect:
        mock_conn = mock_connect.return_value.__enter__.return_value
        mock_cursor = mock_conn.cursor.return_value

        storage.save(data)

        mock_cursor.execute.assert_any_call("CREATE TABLE IF NOT EXISTS api_data (key1, key2)")
        mock_cursor.execute.assert_any_call(
            "INSERT INTO api_data VALUES (?, ?)", ("value1", "value2")
        )
