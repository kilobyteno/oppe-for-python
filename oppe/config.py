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

    BASE_URL = 'https://oppe.app/api/v0'

    # Reading the env variables
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    ENV = os.getenv('OPPE_ENV')
    if ENV == 'staging':
        BASE_URL = 'https://staging.oppe.app/api/v0'

    EVENT_URL = f'{BASE_URL}/event/'
