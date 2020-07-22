#!/bin/bash

DEPTH=1 # change this to an appropriate value if you want to test in different branches
if git log -$DEPTH | grep -qE '^Merge: [0-9a-z].+ [0-9a-z].+$'; then
  BUILDTHIS=$(git diff `git log -$DEPTH | grep -E '^Merge: [0-9a-z].+ [0-9a-z].+$' | awk {'print $2,$3'}` -- domains.txt | grep -E '^\+[0-9a-z].+' | cut -d+ -f2)
  readarray -t arr < <(echo "$BUILDTHIS" | grep -vE '^$|^#')
  for domain in "${arr[@]}"; do
    domain=`echo ${domain} | awk {'print $1'}`
    # Fetch ssl certificates
    ./fetch_cert.py $domain
    # Run dehydrated
    ./dehydrated/dehydrated --config ./config.sh --hook ./hook.py --cron --domain $domain
  done
fi

