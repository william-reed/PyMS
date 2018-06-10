# PyMS
Send text messages from python

## Usage
As found in [example.py](https://github.com/william-reed/PyMS/blob/master/example.py)
```python
from gateways import GATEWAYS
from sender import PyMS

pyms = PyMS()
pyms.connect()
pyms.send_sms('1234567890', GATEWAYS['SPRINT']['SMS_EMAIL'], "Test")
pyms.disconnect()
```
#### Defaults
PyMS uses a few default settings to make this all work. The following inputs can be provided to `PyMS(...)`

* `username` the account username in the form username@domain.com. Defaults to system environment variable `PYMS_USERNAME`
* `password` the password for the account.  Defaults to system environment variable `PYMS_PASSWORD`
* `host` the SMTP server hostname. Defaults to smtp.gmail.com
* `port` the SMTP server port. Defaults to 465

### Gmail
As found out from [radtek](https://stackoverflow.com/users/2023392/radtek) on [Stack Overflow](https://stackoverflow.com/a/27515833/1572848), you need to allow your Gmail account to work with a less secure app by flipping a switch here https://www.google.com/settings/security/lesssecureapps as this type of login is considered unsecure
## Gateways
PyMS uses SMS / MMS gateways to deliver messages to a mobile device. Most US carriers should be provided in the `GATEWAYS` dict in gateways.py for usage. These gateways taken from [here](https://github.com/mfitzp/List_of_SMS_gateways)
## Drawbacks
Currently the carrier of the mobile device must be known to send a message

This may be overcome by hitting http://www.fonefinder.net/ and scraping the results however it presents issues if a user changes there carrier but maintains the same phone number. Most other services are paid for including any API's that exist.
