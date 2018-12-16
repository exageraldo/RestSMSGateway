from rest_sms_getway import RestSMSGetway


client = RestSMSGetway('http://192.168.1.100:8080')

def get_thread_id(phone, pagination=50):
    limit = 0
    while True:
        get_sms_info = client.get_sms(limit=limit)
        phone_list = {sms['address'][-9:]: sms['thread_id'] for sms in get_sms_info['messages']}
        if phone[-9:] in phone_list:
                return phone_list[phone[-9:]]
        elif int(get_sms_info['size']) < int(get_sms_info['limit']):
                return None
        limit += pagination


def get_all_sms(thread_id, pagination=50):
        limit = 0
        while True:
            get_sms_id = client.get_thread(thread_id=thread_id, limit=limit)
            if int(get_sms_id['size']) < int(get_sms_id['limit']):
                break
            limit += pagination
        messages_id = [sms['_id'] for sms in get_sms_id['messages']]
        sms_list = []
        for sms_id in messages_id:
            get_sms = client.get_sms(sms_id=sms_id)
            sms_info = get_sms['sms'][0]
            sms_list.append({sms_info.pop('_id'): sms_info})
        return sms_list


if __name__ == "__main__":
    phone = '+5511987654321'
    thread_id = get_thread_id(phone)
    if not thread_id:
        print("Phone not found")
    else:
        print(get_all_sms(thread_id))