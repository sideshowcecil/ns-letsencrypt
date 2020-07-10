#!/bin/bash
EXITVAL=0

# check for duplicate lines
if [[ $(cat domains.txt | grep -vE '^#|^$' | sort | uniq -d | wc -l) -ne 0 ]]; then
  echo "ERROR: Found duplicate lines in domains.txt file:"
  cat domains.txt | grep -vE '^#|^$' | sort | uniq -d
  EXITVAL=1
fi

# make sure we only have valid domain names
if [[ $(cat domains.txt | grep -vE '^#|^$' | grep -E '\*' | wc -l) -ne 0 ]]; then
  echo "ERROR: Wildcard domains are not supported:"
  cat domains.txt | grep -vE '^#|^$' | grep -E '\*'
  EXITVAL=1
fi

# check for lines starting with *
if [[ $(cat domains.txt | grep -E '^\*' | wc -l) -ne 0 ]]; then
  echo "ERROR: Found a line starting with *:"
  cat domains.txt | grep -E '^\*'
  EXITVAL=1
fi

exit $EXITVAL
