import sqlite3

class CredentialManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_credentials(self, credentials_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT api_key, api_secret FROM credentials WHERE id = ?", (credentials_id,))
            row = cursor.fetchone()
            if row:
                return {"api_key": row[0], "api_secret": row[1]}
            else:
                raise ValueError(f"Credentials with ID {credentials_id} not found")
