from faker import Faker

from oppe.utils import format_tag_name, request_header

fake = Faker()


def test_request_header():
    """ Test request header """
    api_token = fake.sha256()
    header = request_header(api_token=api_token)
    assert header['Accept'] == 'application/json'
    assert header['Content-Type'] == 'application/json'
    assert header['Authorization'] == f'Bearer {api_token}'


def test_format_tag_name():
    """ Test format tag name """
    tag_name = '1.0.0'
    formatted_tag_name = format_tag_name(name=tag_name)
    assert formatted_tag_name == tag_name


def test_format_tag_name_with_wrong_tag_name():
    """ Test format tag name with wrong tag name """
    tag_name = '2.0'
    try:
        format_tag_name(name=tag_name)
    except ValueError as e:
        assert str(e) == f'Wrong tag name: {tag_name}'


def test_format_tag_name_with_wrong_tag_name_2():
    """ Test format tag name with wrong tag name """
    tag_name = '0.0.1+build.1'
    try:
        format_tag_name(name=tag_name)
    except ValueError as e:
        assert str(e) == f'Wrong tag name: {tag_name}'


def test_format_tag_name_with_wrong_tag_name_3():
    """ Test format tag name with wrong tag name """
    tag_name = '0.0.1-rc.1'
    try:
        format_tag_name(name=tag_name)
    except ValueError as e:
        assert str(e) == f'Wrong tag name: {tag_name}'
