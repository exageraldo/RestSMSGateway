class SMSGatewayConnector(object):
    def __init__(self, url, boundary='RestSMSGateway'):
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