import json

import requests

from oppe.config import Config
from oppe.exceptions import EventRequestError, UuidValidationError
from oppe.utils import request_header, validate_uuid


class Oppe:
    """
    Oppe class for communicating with the Oppe API.

    Attributes:
        api_token (str):
            The authentication api_token.
        project_id (str):
            The project_id uuid identifier.
    """

    def __init__(self, api_token, project_id):
        """
        Initialize an instance of the Oppe class.

        :param api_token: The authentication api_token.
        :type api_token: str
        :param project_id: The project_id uuid identifier.
        :type project_id: str
        """
        self.api_token = api_token
        self.project_id = project_id

    def event(self, channel_id, title, description=None, emoji=None, data=None):
        """
        Send an event to the Oppe app.

        :param channel_id: The channel uuid identifier.
        :type channel_id: str
        :param title: The title of the event. Example: "user-registered"
        :type title: str
        :param description: The description of the event. Example: "A new user has registered."
        :type description: str
        :param emoji: An emoji to be displayed with the event. Example: "👋"
        :type emoji: str
        :param data: Any additional data to be sent with the event. Example: {"user_id": 1}
        :type data: object

        :return: True if the event was triggered successfully, False otherwise.
        :rtype: bool

        :raises UuidValidationError: If the channel_id is not a valid UUID.
        :raises EventRequestError: If the event request failed.
        """
        # Validate channel_id
        if not validate_uuid(uuid_input=channel_id):
            raise UuidValidationError(msg='Channel ID must be a valid UUID')

        # Create payload to send to Oppe
        payload = {
            'channel_id': channel_id,
            'title': title,
        }

        # If description is not None, add it to the payload
        if description:
            payload['description'] = description

        # If emoji is not None, add it to the payload
        if emoji:
            payload['emoji'] = emoji

        # If data is not None, add it to the payload
        if data:
            payload['data'] = json.dumps(data)

        # Send request to Oppe
        response = requests.post(Config.EVENT_URL, data=json.dumps(payload), headers=request_header(api_token=self.api_token))
        if response.status_code != 201:
            raise EventRequestError(
                msg=f'Failed to send event to Oppe! Status code: {response.status_code}',
                data=response.json()
            )
        return True
