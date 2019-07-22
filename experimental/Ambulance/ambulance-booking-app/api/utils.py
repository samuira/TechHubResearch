from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
import random
import re
import pyotp

class Utils:

	# Your Account Sid and Auth Token from twilio.com/console
	account_sid = 'AC451c35f95b5057cded94f3b5fbfdc977'
	auth_token = 'e2935ac0460e173a7418c4913ab693d5'
	client = Client(account_sid, auth_token)

	@staticmethod
	def generate_code(digits=4):
		return str(random.randrange(10**(digits-1), 10**digits - 1))

	@staticmethod
	def send_sms(body, to):
		try:
			message = Utils.client.messages.create(
				from_='+12013809078',
				body=body,
				to=to
			)
			return 200, message.status
		except TwilioRestException as e:
			return e.status, e.msg

	@staticmethod
	def find_numbers_re(text):
		return re.findall(r'\d+', text)

	@staticmethod
	def generate_secret_key_hotp():
		return pyotp.random_base32()

	@staticmethod
	def generate_hotp(counter,secret_key):
		hotp = pyotp.HOTP(secret_key, digits=4)
		return hotp.at(counter)

	@staticmethod
	def verify_hotp(otp, counter, secret_key):
		hotp = pyotp.HOTP(secret_key, digits=4)
		return hotp.verify(otp, counter)
