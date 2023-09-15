import json

import requests

from oppe.config import Config
from oppe.utils import request_header


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
        """
        data = {
            'channel_id': channel_id,
            'title': title,
            'description': description,
            'emoji': emoji,
            'data': data
        }
        requests.post(Config.EVENT_URL, data=json.dumps(data), headers=request_header(api_token=self.api_token))
        return True
