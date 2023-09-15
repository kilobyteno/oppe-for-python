import os

from dotenv import load_dotenv
from faker import Faker

from oppe.oppe import Oppe

fake = Faker()

# Reading the env variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def init_oppe():
    """ Initialize Oppe """
    return Oppe(api_token=os.getenv('TEST_API_TOKEN'), project_id=os.getenv('TEST_PROJECT_ID'))


def test_publish_event():
    """ Test publish event """
    oppe = init_oppe()
    response = oppe.trigger_event(channel=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), description=fake.sentence())
    assert response is True
