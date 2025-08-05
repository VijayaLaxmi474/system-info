#!/bin/bash
LOG_FILE="/var/log/syslog" # or use the own file

if [ ! -f "$LOG_FILE" ]; then
  echo " X Log file not found: $LOG_FILE"
  exit 1
fi

echo "Analyzing log file: $LOG_FILE"
echo "_____________________________"
#count total lines 
echo " Total lines:$(wc -l <"$LOG_FILE")"
#count number of errors and warnings
echo " ERROR lines:$(grep -i 'error' "$LOG_FILE" | wc -l)"
echo "WARNING lines:$(grep -i 'warn' "$LOG_FILE" | wc -l)"

#show top 5 frequent error messages"
echo ""
echo "Top 5 frequent ERROR message:"
grep -i 'error' "$LOG_FILE" | awk -F: '{print $NF}' |sort|uniq -c|sort -nr|head -5
echo "DEBUG: I reached here"
