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
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), description=fake.sentence())
    assert response is True


def test_publish_event_with_emoji():
    """ Test publish event with emoji """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), description=fake.sentence(), emoji='👋')
    assert response is True


def test_publish_event_with_data():
    """ Test publish event with data """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), description=fake.sentence(), data={'user_id': 1})
    assert response is True


def test_publish_event_with_emoji_and_data():
    """ Test publish event with emoji and data """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), description=fake.sentence(), emoji='👋', data={'user_id': 1})
    assert response is True


def test_publish_event_with_emoji_and_data_and_no_description():
    """ Test publish event with emoji and data and no description """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), emoji='👋', data={'user_id': 1})
    assert response is True


def test_publish_event_with_emoji_and_no_description():
    """ Test publish event with emoji and no description """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), emoji='👋')
    assert response is True


def test_publish_event_with_data_and_no_description():
    """ Test publish event with data and no description """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word(), data={'user_id': 1})
    assert response is True


def test_publish_event_with_no_description():
    """ Test publish event with no description """
    oppe = init_oppe()
    response = oppe.event(channel_id=os.getenv('TEST_CHANNEL_ID'), title=fake.domain_word())
    assert response is True


def test_publish_event_with_wrong_channel_id():
    """ Test publish event with wrong channel id """
    oppe = init_oppe()
    try:
        oppe.event(channel_id=fake.sha256(), title=fake.domain_word())
    except ValueError as e:
        assert str(e) == 'Channel ID must be a valid UUID'
