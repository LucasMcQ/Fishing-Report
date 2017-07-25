#!/bin/bash

# File: get_report.sh
# Author: Lucas McQuiston
# Purpose: This file will check to see if the current date matches the date
# of the latest fishing report from the AZFGD website. If there is a report
# for that day, the script will extract the fishing report for a particular
# lake that is specified. The info is retrived using the bash command curl.
# The report is then passed into the python script send_report.py to handle
# the html in the report and finally email the specified fishing report to
# the specified email address.


MONTH="$(date +%B)"		# the current month
DAY="$(date +%d)"		# the current day
YEAR="$(date +%Y)"		# the current year

# The AZFGD webpage used to determine if a new fishing report is out.
CHECK_REPORT_URL="https://www.azgfd.com/category/news/"

# AZFGD webpage with the fishing report for the current week.
REPORT_URL="https://www.azgfd.com/fishing-report-$MONTH-$DAY-$YEAR/"


# Check to see if there is a new fishing report present on the AZFGD website.
curl -s $CHECK_REPORT_URL > check_report.txt

CURRENT_REPORT="$(grep "Fishing Report" check_report.txt | head -1)"


# If the current date is not the date on the fishing report, we terminate script.
if [[ $CURRENT_REPORT != *"$MONTH $DAY, $YEAR"* ]]; then
	exit 0
fi


# This will retreive the latest fishing reports in Arizona.
curl -s $REPORT_URL > fishing_report.txt

# Extract the proper lake info from the curl output.
sed -n '/BARTLETT LAKE/,/<p><b>/p' fishing_report.txt > bartlett_report_uncut.txt

# Remove the last line of the file (it is redundant).
head -n -1 bartlett_report_uncut.txt > bartlett_report.txt

# Send the email with the fishing report.
python send_report.py


# Cleanup the mess...
rm bartlett_report_uncut.txt bartlett_report.txt fishing_report.txt check_report.txt config.pyc
