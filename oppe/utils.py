""" Common utilities for the Oppe package """


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
