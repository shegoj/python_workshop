#!/usr/bin/python

from twilio.rest import TwilioRestClient

class SMS_UTILS ():
# Find these values at https://twilio.com/user/account
	def send_sms(self,to_number, msg):
		account_sid = "AC0a4efc346356"
		auth_token = "b3c7e713740"
		client = TwilioRestClient(account_sid, auth_token)
	
		message = client.messages.create(to=to_number, from_="+44",body=msg)

num = "+44"
smsobj = SMS_UTILS()
smsobj.send_sms(num,"")
	
