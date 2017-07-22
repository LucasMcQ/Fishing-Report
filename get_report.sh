#!/bin/bash

MONTH="$(date +%B)"
DAY="$(date +%d)" #"20"
YEAR="$(date +%Y)"
REPORT_URL="https://www.azgfd.com/fishing-report-$MONTH-$DAY-$YEAR/"
CHECK_REPORT_URL="https://www.azgfd.com/category/news/"


# Before we retrive a specific fishing report, we need to check if there is a 
# new fishing report. If there is no new fishing report, we will end the script.
curl $CHECK_REPORT_URL > check_report.txt

CURRENT_REPORT="$(grep "Fishing Report" check_report.txt | head -1)"

# If the current date is not the date on the fishing report, we terminate script.
if [[ $CURRENT_REPORT != *"$MONTH $DAY, $YEAR"* ]]; then
	exit 0
fi




# This will retreive the latest fishing reports in Arizona.
curl $REPORT_URL > fishing_report.txt

# Extract the proper lake info from the curl output.
sed -n '/BARTLETT LAKE/,/<p><b>/p' fishing_report.txt > bartlett_report_uncut.txt

# Remove the last line of the file (it is redundant).
head -n -1 bartlett_report_uncut.txt > bartlett_report.txt

# Send the email with the fishing report.
python send_report.py


# Cleanup the mess...
rm bartlett_report_uncut.txt bartlett_report.txt fishing_report.txt check_report.txt
