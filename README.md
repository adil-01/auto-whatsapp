# auto_whatsapp
Automating WhatsApp using python with custom multiple messaging options, attachment options and supporting images and video sending as well. *auto_whatsapp* also persist your login state once QR code is scanned on web whatsapp.

## Setup
### Installation
In the terminal type the following
```python
pip install auto_whatsapp
```

### Usage
Import *auto_whatsapp* module use its ```sendChat``` function to send messages.
```python
from auto_whatsapp import auto_whatsapp

msg = 'This is a test message'
users = ["user1", "user2", "+91 9876543210"]
auto_whatsapp.sendChat(users, msg)
```
users1 and user2 are saved contact name according to your use case.<br>
Messages can also be send to unsaved contacts like ```+91 9876543210``` as shown above.
Just run the code you can see the magic happening. It will open web whatsapp automatically send the given message to specified users.

> Make sure you have selenium installed <br>```pip install selenium``` <br>and have chromedriver in the same directory. If you don't have chromedriver installed click [here](https://chromedriver.chromium.org/downloads)

___

## Examples
### Sending a document
```python
from auto_whatsapp import auto_whatsapp

users = ["user1", "user2", "+91 9876543210"]
src = 'C:\\Users\\Your_user\\Desktop\\dots.jpg'
auto_whatsapp.sendDoc(users, src)
```

> Note that you have to provide absolute path as src argument and with double backslackes(\\) as shown in example.

___

### Sending a media
Media can be images, videos or audio which whatsapp supports.
```python
from auto_whatsapp import auto_whatsapp

users = ["user1", "user2", "+91 9876543210"]
src = 'C:\\Users\\Your_user\\Desktop\\dots.jpg'
auto_whatsapp.sendMedia(users, src)
```

> Note that you have to provide absolute path as src argument and with double backslackes(\\) as shown in example.

___

## License
*auto_whatsapp* is been licensed under [MIT LICENSE]()