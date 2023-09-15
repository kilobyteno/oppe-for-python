""" Common utilities for the Oppe package """
import re


def request_header(api_token: str) -> dict:
    """
    Make a request header for Oppe's API

    :param api_token: The API Token to be used for authentication
    :type api_token: str
    :return: Authorization Header
    :rtype: dict
    """
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
