import requests


class RestSMSGetway:
    """
    REST SMS Gateway allows to change your phone into a powerful SMS Gateway which you can control from a computer. 
    """

    def __init__(self, url, boundary='RestSMSGetway'):
        """It initialize a connection with the server created by your phone.

        Args:
            url (str): Address showed by the app (after pressing button Start).
            boundary (str, optional): It used in multipart/form-data to separate name/value pairs (it does not exceed 70 bytes in length and consists only of 7-bit US-ASCII characters).

        """
        self.url = f'{url}/v1'
        self.boundary = boundary
        self.headers = {
            'content-type': f"multipart/form-data; boundary=----WebKitFormBoundary{self.boundary}",
            'cache-control': "no-cache"
        }

    def get_thread(self, thread_id=None, limit=10, offset=0):
        """List threads (also know as conversations) available in the mobile phone. The list starts with the recently updated threads. View messages in a thread with a given thread_id.

        Args:
            thread_id (int, optional): Thread to present.
            limit (int, optional): Number of threads to list.
            offset (int, optional): Number of threads to skip.

        Returns:
            requests.models.Response

        """
        if thread_id:
            url = f'{self.url}/thread/{thread_id}/'
            params = {}
        else:
            url = f'{self.url}/thread/'
            params = {'limit': limit, 'offset': offset}
        thread_response = requests.request("GET", f'{url}', headers=self.headers, params=params)
        return thread_response

    def get_sms(self, sms_id=None, limit=10, offset=0):
        """List SMS. The list starts with the newest messages. View SMS with a given sms_id.

        Args:
            sms_id (int, optional): SMS to view.
            limit (int, optional): Number of threads to list.
            offset (int, optional): Number of threads to skip.

        Returns:
            requests.models.Response

        """
        if sms_id:
            url = f'{self.url}/sms/{sms_id}/'
            params = {}
        else:
            url = f'{self.url}/sms/'
            params = {'limit': limit, 'offset': offset}
        sms_response = requests.request("GET", f'{url}', headers=self.headers, params=params)
        return sms_response

    def get_device_status(self):
        """Present basic details about the phone.

        Returns:
            requests.models.Response

        """
        device_status_response = requests.request("GET", f'{self.url}/device/status/', headers=self.headers)
        return device_status_response

    def post_sms(self, phone, message, sim_slot=None):
        """Send SMS. Text from field `message` is sent to phone with a number from field `phone`. Remember that you may be charged for each SMS that you send. Please, use this option wisely.


        Args:
            phone (str): Phone number.
            message (str): Message to send.
            sim_slot (int, optional): Sim slot (sim card) to be used. If sim_slot is incorrect then a default sim card is used.

        Returns:
            requests.models.Response

        """
        payload = (
            f"------WebKitFormBoundary{self.boundary}\r\n"
            f"Content-Disposition: form-data; name=\"message\"\r\n\r\n{message}\r\n"
            f"------WebKitFormBoundary{self.boundary}\r\n"
            f"Content-Disposition: form-data; name=\"phone\"\r\n\r\n{phone}\r\n"
            f"------WebKitFormBoundary{self.boundary}--"
            )
        send_response = requests.request("POST", f'{self.url}/sms/', data=payload, headers=self.headers)
        return send_response
