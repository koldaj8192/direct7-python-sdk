class SMS:

    def __init__(self, client):
        self._client = client

    def send_message(self, params: dict):
        """
        Send a message to a single/multiple recipient.
        :param params: dict - The message request parameters.
        :return:
        """
        return self._client.post(
            self._client.host(),
            "/messages/v1/send",
            params=params
        )

    def get_status(self, request_id: str):
        """
        Get the status for a message request.
        :param params:
        request_id : str - The request ID of the message request.
        :return:
        """
        return self._client.get(
            self._client.host(),
            f"/report/v1/message-log/{request_id}"
        )
