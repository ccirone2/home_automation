# nest_monitor/auth.py
import anvil.secrets
import requests


def setup_nest_credentials():
    """
    Get OAuth2 credentials from Anvil Secrets.

    Returns:
        dict: A dictionary containing client_id, client_secret, and refresh_token.
    """
    return {
        "client_id": anvil.secrets.get_secret("nest_client_id"),
        "client_secret": anvil.secrets.get_secret("nest_client_secret"),
        "refresh_token": anvil.secrets.get_secret("nest_refresh_token"),
    }


def get_access_token(credentials):
    """
    Get a new access token using the refresh token.

    Args:
        credentials (dict): A dictionary containing client_id, client_secret, and refresh_token.

    Returns:
        str: The new access token.
    """
    token_url = "https://www.googleapis.com/oauth2/v4/token"
    data = {
        "client_id": credentials["client_id"],
        "client_secret": credentials["client_secret"],
        "refresh_token": credentials["refresh_token"],
        "grant_type": "refresh_token",
    }
    response = requests.post(token_url, data=data)
    return response.json()["access_token"]
