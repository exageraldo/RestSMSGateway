
# RestSMSGetway :love_letter:

  >Unofficial Library

REST SMS Gateway allows to change your phone into a powerful SMS Gateway which you can control from a computer.

  

## Getting Started

  

> Note: The computer (that will run the script) and your phone have to be connected on the same network. **Android only!**

  First of all, you have to install [Rest SMS Getway](bit.ly/RestSMSGetway) on your Android phone.

Open the app and press the `start` button. You'll need the IP address shown in there (e.g, `http://172.16.19.77:8080`).



### Installing

  

Easy-peasy! You only need to run one command

```
pip install -e /path/to/RestSMSGetway -U 
```
or, go to the path and run
```
pip install -e . -U 
```

 

## Running the tests
>Note: My mistake!

We don't have test yet.

  

## Examples
Import and configure the client:
```python
>>> from rest_sms_getway import RestSMSGetway 
>>> client = RestSMSGetway('http://172.16.19.77:8080')
```

Now, you can do what you want (or almost)!

Let's list all conversations available in the mobile phone:
```python
threads = getway.get_thread() 
threads.json()
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


>>> threads = getway.get_thread() 
>>> threads.json()
#OUTPUT
# {'threads': [{'timestamps': {'update': '1544785173349'}, '_id': '95'},
# {'timestamps': {'update': '1544751618760'}, '_id': '94'}],
# 'size': 2,
# 'limit': '2',
# 'offset': '0'}
```

And now, send a message!
```python
sender = getway.post_sms('+5511987654321', 'Your first message')
if send.ok: # or status_code == 200
    print('Message sent!')
```
  

## Authors

  

*  **Geraldo Castro** - *Just for fun!* - [exageraldo](https://github.com/exageraldo)

  

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

  

## License

 
 This project is licensed under the GNU Lesser General Public License v3 (LGPLv3) - see the [LICENSE.md](LICENSE.md) file for details

  

## Acknowledgments

  * Python Community
