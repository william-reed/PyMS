from gateways import GATEWAYS
from sender import PyMS

pyms = PyMS()
pyms.connect()
pyms.send_sms('1234567890', GATEWAYS['SPRINT']['SMS_EMAIL'], "Test")
pyms.disconnect()
