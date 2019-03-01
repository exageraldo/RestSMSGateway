import logging
from rest_sms_gateway import SMSGatewayClient
    

class SMSHandler(logging.StreamHandler):
    def __init__(self, address, phone_route):
        super().__init__(self)
        self.address = address
        self.client = SMSGatewayClient(phone_route)

    def emit(self, record):
        msg = self.format(record)
        self.client.send_sms(self.address, msg)


if __name__ == '__main__':
    sms_log = SMSHandler('+5511987654321', 'http://your.link.here:8080')
    logger = logging.getLogger(__name__)
    logger.addHandler(sms_log)
    logger.critical('This is a message from a log!')