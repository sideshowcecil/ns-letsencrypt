#!/bin/bash

# Base
NSLE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DEHYDRATED="${NSLE}/dehydrated/dehydrated"
CONFIG="${NSLE}/config.sh"
HOOK="${NSLE}/ns-hook.sh"

# Control files used by hooks
export counter_file=$(mktemp "${NSLE}/.counter.XXXXXX")
export connect_file=$(mktemp "${NSLE}/.connect.XXXXXX")
printf '%s\n' "0" >"$connect_file"

# Normal usage
$DEHYDRATED -c -f $CONFIG -k $HOOK
# Cleanup unused certs
$DEHYDRATED -gc -f $CONFIG
