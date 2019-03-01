from rest_sms_gateway.client import SMSGatewayClient 
import time


class Message(SMSGatewayClient):
    def __init__(self, url, boundary='RestSMSGateway'):
        super().__init__(url, boundary)

    @property
    def message_count(self):
        all_messages = self.get_all()
        return len(all_messages)

    @property
    def ids(self):
        infos = self.get_all()
        _ids = [message['_id'] for message in infos['messages']]
        return _ids

    def get_all(self):
        return self.get_sms(limit=self._max_rate)

    def get_by_id(self, sms_id):
        return self.get_sms(sms_id=sms_id, limit=self._max_rate)

    def bulk_sms(self, message, address_list, amount=1, safe_mode=True):
        def _safe_count(msg_number):
            if (msg_number+1) % 30 == 0:
                time.sleep(30)
            else:
                time.sleep(1.5)
                
        for address in address_list:
            for message_count in range(amount):
                self.send_sms(address, message)
                if safe_mode:
                    _safe_count(message_count)
            print(f'All messages to {address} have been sent')
    