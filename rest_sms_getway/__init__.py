import requests


class RestSMSGetway(object):
    """
    REST SMS Gateway allows to change your phone into a powerful SMS Gateway which you can control from a computer. 
    """

    def __init__(self, url, boundary='RestSMSGetway'):
        """Initialize a connection with the server created by your phone.

        Args:
            url (str): Address showed by the app (after pressing button Start).
            boundary (str, optional): It used in multipart/form-data to separate name/value pairs (it does not exceed 70 bytes in length and consists only of 7-bit US-ASCII characters).
        
        Attributes:
            headers (dict): Header to be sent in requests.
            last_request (requests.models.Response): More info about last request.

        """
        self.url = f'{url}/v1'
        self.boundary = boundary
        self.headers = {
            'content-type': f"multipart/form-data; boundary=----WebKitFormBoundary{self.boundary}",
            'cache-control': "no-cache"
        }
        self.last_request = None

    def get_thread(self, thread_id=None, limit=10, offset=0):
        """List threads (also know as conversations) available in the mobile phone. The list starts with the recently updated threads. View messages in a thread with a given thread_id.

        Args:
            thread_id (int, optional): Thread to present.
            limit (int, optional): Number of threads to list.
            offset (int, optional): Number of threads to skip.

        Returns:
            dict: Info about conversations.
            
            Return with no thread_id:
            {
                threads: [
                    {
                        timestamps: {
                            update (str): Last update time in milliseconds
                        }, 
                        _id (str): Thread ID
                    },
                ],
                size (int): Number of listed messages,
                limit (str): Number of threads to list,
                offset (str): Number of threads to skip
            }

            Return with thread_id:
            {
                messages: [
                    {
                        _id (str): Thread ID,
                        timestamps: {
                            sent (str): Sent time in milliseconds
                        },
                        type (str): Message Type (e.g SMS, MMS),
                        msg_box (str) : Incoming or outgoing message
                    }
                ],
                limit (str): Number of threads to list,
                offset (str): Number of threads to skip
                size: Number of listed messages
            }

        """
        if thread_id:
            url = f'{self.url}/thread/{thread_id}/'
        else:
            url = f'{self.url}/thread/'
        params = {'limit': limit, 'offset': offset}
        thread_response = requests.get(url, headers=self.headers, params=params)
        self.last_request = thread_response
        response = thread_response.json()
        return response

    def get_sms(self, sms_id=None, limit=10, offset=0):
        """List SMS. The list starts with the newest messages. View SMS with a given sms_id.

        Args:
            sms_id (int, optional): SMS to view.
            limit (int, optional): Number of threads to list.
            offset (int, optional): Number of threads to skip.

        Returns:
            dict: 

            Return with no sms_id:
            {
                limit (str): Number of threads to list,
                offset (str): Number of threads to skip,
                size (str): Number of listed messages,
                messages: [
                    {
                        address (str): Phone number where the message was sent to,
                        thread_id (str): Thread ID,,
                        body (str): Message content,
                        _id (str): Message ID,
                        timestamps: {
                            delivery (str): Sent time in milliseconds
                        },
                        msg_box (str): Incoming or outgoing message
                    }
                ]
            }

            Return with sms_id:
            {
                sms: [
                    {
                        address (str): Phone number where the message was sent to,
                        thread_id (str): Thread ID,
                        body (str): Message content,
                        _id (str): Message ID,
                        timestamps: {
                            delivery (str): Sent time in milliseconds
                        },
                        msg_box (str): Incoming or outgoing message
                    }
                ]
            }

        """
        if sms_id:
            url = f'{self.url}/sms/{sms_id}/'
            params = {}
        else:
            url = f'{self.url}/sms/'
            params = {'limit': limit, 'offset': offset}
        sms_response = requests.get(url, headers=self.headers, params=params)
        self.last_request = sms_response
        response = sms_response.json()
        return response

    def get_device_status(self):
        """Present basic details about the phone.

        Returns:
            dict: Info about host device.

            {
                timestamp (int): Current time in milliseconds,
                is_airplane_mode: ,
                telephony: {
                    is_network_roaming (bool): Is roaming present (true) or not (false),
                    sim_state (str): SIM state (supported values: ready, absent, unknown, pin required, puk required, network locked),
                    network_operator_name (str): Network operator name
                },
                'telephonies': [
                    {
                        network_operator_name (str): Network operator name,
                        carrier_name (str): Carrier name,
                        is_network_roaming (str): Is roaming present (true) or not (false) (if available, requires OS v. 7.0),
                        sim_state (int): Sim slot number,
                        display_name (str): Carrier name set by user,
                        sim_slot (int): Sim slot number
                    }
                ],
                'battery': {
                    status (str): Power status (supported values: charging, full, discharging, not charging, unknown), 
                    level (float): Battery level
                }
            }

        """
        device_status_response = requests.get(f'{self.url}/device/status/', headers=self.headers)
        self.last_request = device_status_response
        response = device_status_response.json()
        return response

    def send_sms(self, phone, message, sim_slot=None):
        """Send SMS. Text from field `message` is sent to phone with a number from field `phone`. Remember that you may be charged for each SMS that you send. Please, use this option wisely.


        Args:
            phone (str): Phone number.
            message (str): Message to send.
            sim_slot (int, optional): Sim slot (sim card) to be used. If sim_slot is incorrect then a default sim card is used.

        Returns:
            dict:
            {
                'ok' (bool): True, if the message was sent (200), False if not,
                'status_code (int): Requisition status code
            }

        """
        payload = (
            f"------WebKitFormBoundary{self.boundary}\r\n"
            f"Content-Disposition: form-data; name=\"message\"\r\n\r\n{message}\r\n"
            f"------WebKitFormBoundary{self.boundary}\r\n"
            f"Content-Disposition: form-data; name=\"phone\"\r\n\r\n{phone}\r\n"
            f"------WebKitFormBoundary{self.boundary}--"
            )
        send_response = requests.post(f'{self.url}/sms/', data=payload, headers=self.headers)
        self.last_request = send_response
        if send_response.status_code == 200:
            return {'ok': True, 'status_code': 200}
        return {'ok': False, 'status_code': send_response.status_code}
