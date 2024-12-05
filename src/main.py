import argparse
from api_connector import APIConnector
from credential_manager import CredentialManager
from data_storage import DataStorage

def main():
    parser = argparse.ArgumentParser(description="CLI script for API interaction")

    # To specify which credentials to use.
    parser.add_argument("--credentials_id", type=int, required=True, help="ID of the credentials to use")
    
    # To specify whether to store the data in JSON, CSV, or SQLite format.
    parser.add_argument("--storage_format", choices=["json", "csv", "sqlite"], required=True, help="Storage format")
    
    # To specify the path where to store the data using JSON or CSV file
    parser.add_argument("--storage_path", type=str, required=True, help="Path to store the data")

    args = parser.parse_args()

    # Fetch credentials
    credential_manager = CredentialManager("credentials.db")
    credentials = credential_manager.get_credentials(args.credentials_id)

    # API interaction
    api_connector = APIConnector("http://localhost", credentials["api_key"], credentials["api_secret"])
    data1 = api_connector.fetch_data("/api/v1/data")
    data2 = api_connector.fetch_data("/api/v1/other_data")
    combined_data = data1 + data2

    # Save data
    data_storage = DataStorage(args.storage_format, args.storage_path)
    data_storage.save(combined_data)

if __name__ == "__main__":
    main()
