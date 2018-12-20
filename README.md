
# RestSMSGateway :love_letter:

  >Unofficial Library

REST SMS Gateway allows to change your phone into a powerful SMS Gateway which you can control from a computer.

  

## Getting Started

  

> Note: The computer (that will run the script) and your phone have to be connected on the same network. **Android only!**

  First of all, you have to install [Rest SMS Gateway](http://bit.ly/RestSMSGateway) on your Android phone.

Open the app and press the `start` button. You'll need the IP address shown in there (e.g, `http://172.16.19.77:8080`).



### Installing

  

Easy-peasy! You only need to run one command

```
pip install rest-sms-gateway
```

 

## Running the tests
>Note: My mistake!

We don't have test yet.

  

## Examples
Import and configure the client:
```python
>>> from rest_sms_gateway import SMSGatewayClient 
>>> client = SMSGatewayClient('http://172.16.19.77:8080')
```

Now, you can do what you want (or almost)!

Let's list all conversations available in the mobile phone:
```python
>>> client.get_thread() 

#OUTPUT
# {'threads': [{'timestamps': {'update': '1544785173349'}, '_id': '95'},
# {'timestamps': {'update': '1544751618760'}, '_id': '94'},
# {'timestamps': {'update': '1544751384521'}, '_id': '93'},
# {'timestamps': {'update': '1544115829308'}, '_id': '92'},
# {'timestamps': {'update': '1543572583029'}, '_id': '91'},
# {'timestamps': {'update': '1543275852269'}, '_id': '90'},
# {'timestamps': {'update': '1544204987635'}, '_id': '89'},
# {'timestamps': {'update': '1541087704128'}, '_id': '88'},
# {'timestamps': {'update': '1540053558537'}, '_id': '87'},
# {'timestamps': {'update': '1539808989397'}, '_id': '86'}],
# 'size': 10,
# 'limit': '10',
# 'offset': '0'}


>>> client.get_thread(limit=2) 

#OUTPUT
# {'threads': [{'timestamps': {'update': '1544785173349'}, '_id': '95'},
# {'timestamps': {'update': '1544751618760'}, '_id': '94'}],
# 'size': 2,
# 'limit': '2',
# 'offset': '0'}
```

And now, send a message!
```python
>>> sender = client.send_sms('+5511987654321', 'Your first message') # Single SMS
>>> if sender['ok']: # or sender['status_code'] == 200
...     print('Message sent!')

# OR

>>> friends_numbers = ['+5511987654321', '+5511987654322', '+5511987654323']
>>> for friend in friends_numbers: # Bulk SMS 
...     client.send_sms(friend, "Hey, let's play BroForce!")
```



## Attention

If you're trying to send lot of messages at once, [read this article](https://forums.androidcentral.com/google-nexus-4/227096-messaging-sending-large-amount-messages.html) about "`Messaging is sending a large amount of messages`".

In my tests, this notification only appears after sending 30 messages. An alternative way out for this is:

```python
>>> from rest_sms_gateway import SMSGatewayClient
>>> import time
>>> client = SMSGatewayClient('http://172.16.19.77:8080')
>>> for msg_number in range(60):
...     client.send_sms('+5511987654321', 'Your msg here!')
...     if (msg_number+1) % 30 == 0:
...         # Every 30 messages, an interval of 30 seconds is given
...         time.sleep(30)
...     else:
...         # An interval of 1.5 seconds is given for each message
...         time.sleep(1.5)
```

Also be careful with your phone carrier, they may be slow with the high demand for messages and/or send the messages out of order.



## Authors

  

*  **Geraldo Castro** - *Just for fun!* - [exageraldo](https://github.com/exageraldo)

  

See also the list of [contributors](https://github.com/exageraldo/RestSMSGateway/contributors) who participated in this project.

  

## License

 
 This project is licensed under the GNU Lesser General Public License v3 (LGPLv3) - see the [LICENSE](LICENSE) file for details

  

## Acknowledgments

  * Python Community
  * [Tyrone Damasceno](https://github.com/tyronedamasceno) for trying the code and finding bugs
  * [Sedir Morais](https://github.com/sedir) for reviewing the code and finding errors.
