import requests
from oppe.config import Config
import json


class Oppe:
    """
    Oppe class for triggering events in the Oppe app.

    Attributes:
        token (str):
            The authentication token.
        project (str):
            The project identifier.
        """
    def __init__(self, token, project):
        """
          Initializes an instance of the Oppe class.

          :param token: The authentication token.
          :type token: str
          :param project: The project identifier.
          :type project: str
          """
        self.token = token
        self.project = project

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
            "channel_id": channel,
            "title": title,
            "description": description,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(Config.EVENT_URL, data=json.dumps(data), headers=headers)
        return True

