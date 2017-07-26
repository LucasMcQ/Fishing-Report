# Fishing-Report

This program will email you the current fishing report for a lake that you
want that is in Arizona. The fishing report is pulled from the AZFGD website.
A bash script pulls the data from the AZFGD website and finds the lake
specified and sends the report into a python script to send the email of the
fishing report to the specified email addresses.

# To Run:

cd .../fishing-report
chmod +x get_report.sh
python send_report.py

After the script has been executed, if the current date is the date of the
most recent fishing report, then an email of the fishing report for the
specified lake will be emailed to the specified email addresses.
