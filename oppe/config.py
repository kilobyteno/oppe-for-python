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

    BASE_URL = 'https://oppe.app/api'

    # Reading the env variables
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    ENV = os.getenv('ENV')
    if ENV == 'staging':
        BASE_URL = 'https://staging.oppe.app/api'

    EVENT_URL = f'{BASE_URL}/event/'
