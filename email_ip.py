#! /usr/bin/python

import smtplib
import datetime
import requests
import json
import creds

ip_url = "http://www.telize.com/jsonip"
gmail_user = creds.gmail_user
gmail_pw = creds.gmail_pw
recvr = creds.recvr
date = datetime.datetime.now().strftime("%m-%d-%Y")

r = requests.get(ip_url)
j = json.loads(r.content)
ip = j["ip"]

header = "To: " + recvr + "\n" + "From: " + gmail_user + "\n" + "Subject: Current Home IP is: " + ip + " on " + date + "\n"
msg = header + "\n" + ip + "\n"

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pw)

print msg

smtpserver.sendmail(gmail_user, recvr, msg)

print "\n" + "Done!" + "\n"

smtpserver.close()