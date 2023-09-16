""" Common utilities for the Oppe package """
import re
import uuid

from oppe.exceptions import ApiTokenMissingError


def request_header(api_token: str) -> dict:
    """
    Make a request header for Oppe's API

    :param api_token: The API Token to be used for authentication
    :type api_token: str
    :return: Authorization Header
    :rtype: dict

    :raises ApiTokenMissingError: If the API Token is empty
    """
    # Check if the API Token is empty
    if not api_token:
        raise ApiTokenMissingError(msg='API Token cannot be empty')

    return {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_token}'
    }


def format_tag_name(name: str) -> str:
    """
    Format tag name to be used in the release notes

    :param name:
    :type name: str
    :return: Correctly formatted tag name
    :rtype: str
    :raises ValueError: If tag name is not formatted correctly
    """
    pattern = re.compile(r'^\d+\.\d+\.\d+$')
    match = pattern.search(name)

    # Check if the tag name is formatted correctly
    if match:
        return name

    # If the tag name is not formatted correctly, raise an error
    raise ValueError(f'Wrong tag name: {name}')


def validate_uuid(uuid_input: str) -> bool:
    """
    Validate if input string is a valid UUID

    :param uuid_input: UUID string
    :type uuid_input: str
    :return: True if input is a valid UUID, False otherwise
    :rtype: bool
    """
    if uuid_input is None:
        return False
    try:
        uuid.UUID(uuid_input)
    except ValueError:
        return False
    return True
