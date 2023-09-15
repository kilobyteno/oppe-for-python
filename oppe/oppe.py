import json

import requests

from oppe.config import Config


class Oppe:
    """
    Oppe class for triggering events in the Oppe app.

    Attributes:
        api_token (str):
            The authentication api_token.
        project_id (str):
            The project_id identifier.
    """

    def __init__(self, api_token, project_id):
        """
        Initialize an instance of the Oppe class.

        :param api_token: The authentication api_token.
        :type api_token: str
        :param project_id: The project_id identifier.
        :type project_id: str
        """
        self.api_token = api_token
        self.project_id = project_id

    def trigger_event(self, channel, title, description):
        """
        Triggers an event in the Oppe app.

        :param channel: The channel identifier.
        :type channel: str
        :param title: The title of the event.
        :type title: str
        :param description: The description of the event.
        :type description: str

        :return: True if the event was triggered successfully, False otherwise.
        :rtype: bool
        """
        data = {
            'channel_id': channel,
            'title': title,
            'description': description,
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_token}'
        }
        requests.post(Config.EVENT_URL, data=json.dumps(data), headers=headers)
        return True
