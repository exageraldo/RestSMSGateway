from rest_sms_gateway.client import SMSGatewayClient
import requests

class Conversation(SMSGatewayClient):
    def __init__(self, url, boundary='RestSMSGateway', max_rate=100000):
        super().__init__(url, boundary, max_rate)

    @property
    def thread_count(self):
        all_threads = self.get_all()
        return len(all_threads['threads'])
    
    @property
    def ids(self):
        infos = self.get_all()
        _ids = [thread['_id'] for thread in infos['threads']]
        return _ids

    def get_all(self):
        return self.get_thread(limit=self._max_rate)

    def get_by_id(self, thread_id):
        return self.get_thread(thread_id=thread_id, limit=self._max_rate)

    def get_by_number(self, phone):
        for _id in self.ids:
            # Get one sms id from a thread list
            get_thread = self.get_thread(thread_id=_id, limit=1)
            thread = get_thread['messages']
            msg_id = thread[0]['_id']
            # Find a number from a sms id
            get_sms = self.get_sms(sms_id=msg_id, limit=1)
            sms = get_sms['sms']
            phone_sent = sms[0]['address']
            # Match the numbers
            if not (phone == phone_sent):
                continue
            phone_thread = self.get_by_id(_id)
            # Add a phone in found dict info
            phone_thread.update({
                'phone': phone
            })
            return phone_thread
        return {'phone': phone}


