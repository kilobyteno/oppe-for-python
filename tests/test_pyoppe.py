import os

from dotenv import load_dotenv

from oppe.oppe import Oppe

# Reading the env variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def init_oppe():
    """ Initialize Oppe """
    return Oppe(token=os.getenv('TEST_API_TOKEN'), project=os.getenv('TEST_PROJECT'))


def test_publish_event():
    """ Test publish event """
    oppe = init_oppe()
    response = oppe.trigger_event(channel=os.getenv('TEST_CHANNEL_ID'), title=os.getenv('TEST_TITLE'), description=os.getenv('TEST_DESCRIPTION'))
    assert response is True
