#!/bin/bash
CERTNAMES=`cat domains.txt | awk {'print $1'} | grep -vE '^#|^$'`
# Fetch ssl certificates
for CERTNAME in $CERTNAMES; do
  ./fetch_cert.py $CERTNAME
done
