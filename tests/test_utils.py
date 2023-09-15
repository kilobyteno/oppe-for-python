from faker import Faker

from oppe.utils import request_header

fake = Faker()


def test_request_header():
    """ Test request header """
    api_token = fake.sha256()
    header = request_header(api_token=api_token)
    assert header['Accept'] == 'application/json'
    assert header['Content-Type'] == 'application/json'
    assert header['Authorization'] == f'Bearer {api_token}'
