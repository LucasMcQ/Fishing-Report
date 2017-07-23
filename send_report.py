#!/usr/bin/python

# Funtion: send_email_from_gmail()
# Returns: void
# Author: Lucas McQuiston
# Description: 

import config
import smtplib
import time
import imaplib
import email


def send_email_from_gmail():

	# Save the operation to be performed into the operation var	
	with open('bartlett_report.txt', 'r') as myfile:
		TEXT = myfile.read()

	# The message that will be sent in the email.		
	message = TEXT

        parsed_message = ""

        i = 0

        while(i < len(message)):

            if(message[i] == '<'):
                i = scan_past_html(message, i)

            if(message[i] == '&'):
                while(message[i] != ';'):
                    i+=1
                i+=1

            parsed_message += message[i]
            i+=1


	# Send the email -- David Okwii
	# User: stackoverflow.com/users/547050/david-okwii
	# Post: stackoverflow.com/questions/1014755/how-to-send-email-with-gmail-as-provider-using-python
	try:
		
		server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
		server.ehlo()
		server.starttls()
		server.login(config.FROM_EMAIL, config.FROM_PWD)
		server.sendmail(config.FROM_EMAIL, config.TO, parsed_message)
		server.close()

	except Exception, e:
		print str(e)




def scan_past_html(message, i):

    while(message[i] != '>'):
        i += 1
    
    i += 1

    if(message[i] == '<'):
        i = scan_past_html(message, i)
    
    return i



send_email_from_gmail()
