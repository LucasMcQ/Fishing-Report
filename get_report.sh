#!/bin/bash

MONTH="$(date +%B)"
DAY="20" #"$(date +%d)"
YEAR="$(date +%Y)"
URL="https://www.azgfd.com/fishing-report-$MONTH-$DAY-$YEAR/"

curl $URL > fishing_report.txt

sed -n '/BARTLETT LAKE/,/<p><b>/p' fishing_report.txt > bartlett_report_uncut.txt

head -n -1 bartlett_report_uncut.txt > bartlett_report.txt


python send_report.py
