
#!/usr/bin/python

# Funtion: send_email_from_gmail()
# Returns: void
# Author: Lucas McQuiston
# Description:


import smtplib
import time
import imaplib
import email

TO          = "RECIVING EMAIL ADDRESS"
FROM_EMAIL  = "SENDING EMAIL ADDRESS"
FROM_PWD    = "SENDING EMAIL PASSWORD"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587


def send_email_from_gmail():

	# Save the operation to be performed into the operation var	
	with open('bartlett_report.txt', 'r') as myfile:
		TEXT = myfile.read()


	# The message that will be sent in the email.		
	message = TEXT

        parsed_message = ""

        i = 0

        while i < len(message):

            if message[i] == '<':
                while message[i] != '>':
                    i+=1
                i+=1
                if message[i] == '<':
                    while message[i] != '>':
                        i+=1
                    i+=1
                    if message[i] == '<':
                        while message[i] != '>':
                            i+=1
                        i+=1

            if message[i] == '&':
                while message[i] != ';':
                    i+=1
                i+=1

            parsed_message += message[i]
            i+=1


	# Send the email -- David Okwii
	# User: stackoverflow.com/users/547050/david-okwii
	# Post: stackoverflow.com/questions/1014755/how-to-send-email-with-gmail-as-provider-using-python
	try:
		
		server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		server.ehlo()
		server.starttls()
		server.login(FROM_EMAIL, FROM_PWD)
		server.sendmail(FROM_EMAIL, TO, parsed_message)
		server.close()

	except Exception, e:
		print str(e)


send_email_from_gmail()
