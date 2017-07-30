#!/usr/bin/python

# Funtion: send_email_from_gmail()
# Returns: void
# Author: Lucas McQuiston
# Description: 

import sys
import smtplib
import config
import imaplib
import email



TO = sys.argv[1]        # the email that the script will send the fishing report to

def send_email_from_gmail():

	# Save the operation to be performed into the operation var	
	with open('lake_report.txt', 'r') as myfile:
		TEXT = myfile.read()

	# The message that will be sent in the email.		
	message = TEXT

        parsed_message = ""     # final message that will be emailed

        i = 0       # index of the message

        while(i < len(message)):

            if(message[i] != '<' and message[i] != '&'):
                parsed_message += message[i]
                i+=1
            else:

                if(message[i] == '&'):
                    while(message[i] != ';'):
                       i+=1
                    i+=1
                else:
                    while(message[i] != '>'):
                       i += 1
                    i += 1



	# Send the email -- David Okwii
	# User: stackoverflow.com/users/547050/david-okwii
	# Post: stackoverflow.com/questions/1014755/how-to-send-email-with-gmail-as-provider-using-python
	try:
		
		server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
		server.ehlo()
		server.starttls()
		server.login(config.FROM_EMAIL, config.FROM_PWD)
		server.sendmail(config.FROM_EMAIL, TO, parsed_message)
		server.close()

	except Exception, e:
		print str(e)


send_email_from_gmail()
