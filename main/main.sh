#!/bin/sh
tcpdump -i eth0 -s 0 -A 'tcp dst port 80 or tcp dst port 443' -l > httptraffic.txt