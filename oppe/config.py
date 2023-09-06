import os

from dotenv import load_dotenv


class Config:
    """
    Configuration class for Oppe app settings

    Attributes:
        BASE_URL (str):
            The base URL for the Oppe app
        EVENT_URL (str):
            The URL for accessing Oppe app events
    """
    # Reading the env variables
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    BASE_URL = f"https://{os.getenv('ENV')}oppe.app"
    EVENT_URL = f"{BASE_URL}/api/event/"
