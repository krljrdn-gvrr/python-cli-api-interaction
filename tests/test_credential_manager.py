import pytest
from unittest.mock import MagicMock
from src.credential_manager import CredentialManager

@pytest.fixture
def mock_db_connection(mocker):
    return mocker.patch("sqlite3.connect", autospec=True)

def test_get_credentials_success(mock_db_connection):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ("test_key", "test_secret")
    mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

    manager = CredentialManager(db_path="test.db")
    credentials = manager.get_credentials(1)

    mock_cursor.execute.assert_called_once_with("SELECT api_key, api_secret FROM credentials WHERE id = ?", (1,))
    assert credentials == {"api_key": "test_key", "api_secret": "test_secret"}

def test_get_credentials_failure(mock_db_connection):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

    manager = CredentialManager(db_path="test.db")
    with pytest.raises(ValueError, match="Credentials with ID 1 not found"):
        manager.get_credentials(1)
