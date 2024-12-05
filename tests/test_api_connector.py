import pytest
from unittest.mock import patch
from src.api_connector import APIConnector

@pytest.fixture
def api_connector():
    return APIConnector(base_url="http://localhost", api_key="test_key", api_secret="test_secret")

@patch("src.api_connector.requests.get")
def test_fetch_data_success(mock_get, api_connector):
    # Mock the API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"data": "test_data"}

    endpoint = "/api/v1/data"
    result = api_connector.fetch_data(endpoint)

    # Assertions
    mock_get.assert_called_once_with(
        "http://localhost/api/v1/data",
        headers={"Authorization": "Bearer test_key:test_secret"}
    )
    assert result == {"data": "test_data"}

@patch("src.api_connector.requests.get")
def test_fetch_data_failure(mock_get, api_connector):
    # Mock a failure response
    mock_get.return_value.status_code = 404
    mock_get.return_value.text = "Not Found"

    with pytest.raises(Exception, match="API request failed: 404, Not Found"):
        api_connector.fetch_data("/api/v1/data")
