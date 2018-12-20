from rest_sms_gateway import SMSGatewayClient


client = SMSGatewayClient('http://172.16.19.77:8080')

def send_message(phone, message):
    sms = client.send_sms(phone=phone, message=message)
    if sms['ok']:
        get_last_sms = client.get_sms(limit=1)
        last_sms = get_last_sms['messages'][0]
        verify_phone = last_sms['address'][-9:] == phone[-9:]
        verify_message = last_sms['body'] == message
        if verify_phone and verify_message:
            return (
                "Message sent and verified successfully!\n"
                f"Status code: {sms['status_code']}\n"
                f"Thread ID: {last_sms['thread_id']}\n"
                f"SMS ID: {last_sms['_id']}"
            )
        return(
            "Message sent but not verified\n"
            f"Status code: {sms['status_code']}"
        )
    return(
        "Message not sent!\n"
        f"Status code: {sms['status_code']}\n"
    )


if __name__ == "__main__":
    phone = '+5511987654321'
    message = 'This is my message!'
    send = send_message(phone, message)
    print(send)