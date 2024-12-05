# Python CLI API Interaction

## Overview of the Solution:

Since the instructions didn't say that I should use a Python framework, my method entails writing a Python CLI script that communicates with two API endpoints, dynamically pulls API credentials from a database, and stores the obtained data locally in a format of the user's choosing (JSON, CSV, or SQLite). Modularity, maintainability, and conformity to Python best practices were the key points of emphasis.A Python CLI script that interacts with an API. The script will do the following:

### The implementation:

-   Retrieves credentials using a CredentialManager class.
-   Fetches data from API endpoints using an APIConnector class.
-   Stores the data locally using a DataStorage class.
-   Orchestrates these components via a CLI interface in main.py.


## Design Patterns Used

### Singleton Pattern:

-   To guarantee that a specific API key and secret are only used in one instance, use APIConnector.
-   Prevents needless startup and guarantees reliable resource use.

### Factory Pattern:

-   The method of obtaining credentials from the database is abstracted in CredentialManager.
-   Allows for future modifications to the data source by encapsulating the credential retrieval logic.

### Strategy Pattern:

-   To enable dynamic storage mechanism selection (JSON, CSV, or SQLite) in DataStorage.
-   Allows new storage formats to be added without changing the logic that is already in place.

### Facade Pattern:

-   Main.py is used to give users a straightforward interface through which they may interact with sophisticated modules such as data storage, credential management, and API processing.
-   Coordinates the underlying components and streamlines the CLI interface.


## File Organization

To guarantee clarity and maintainability, the solution is separated into logical modules:

```project_root/
│
├── src/
│   ├── api_connector.py        # Handles API interaction logic
│   ├── credential_manager.py   # Retrieves credentials from the database
│   ├── data_storage.py         # Manages local data storage
│   └── main.py                 # CLI interface and orchestrates the workflow
│
├── tests/
│   ├── test_api_connector.py   # Tests for APIConnector functionality
│   ├── test_credential_manager.py  # Tests for CredentialManager functionality
│   ├── test_data_storage.py    # Tests for DataStorage functionality
│
├── credentials.db              # SQLite database storing API credentials
├── README.md                   # Project overview and usage instructions
├── requirements.txt            # Dependencies for the project
└── .gitignore                  # Specifies files to exclude from version control

```

## TESTING

Verifying each component's functionality, modularity, and robustness as well as the workflow as a whole are all part of the testing process. Below is a summary of the methodology:

### Key Areas of Focus

1. Unit Testing:
        
        Each module (api_connector.py, credential_manager.py, data_storage.py) is tested independently to ensure functionality.
2. Mock external dependencies to isolate the logic under test. Integration Testing:

        Test how the modules interact with each other when orchestrated by main.py.
        Verify that API credentials are retrieved, data is fetched from endpoints, and stored correctly in the specified format.

3. Error Handling:

        Test edge cases, such as missing or invalid credentials, API failures, and unsupported storage formats.

4. Performance:

        Measure how the system handles larger datasets or slow API responses.
        Test the efficiency of data storage methods (JSON, CSV, SQLite).

5. CLI Interface:

        Test the command-line arguments to ensure the correct parameters are accepted and passed to the modules.
