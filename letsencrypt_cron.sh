#!/bin/bash

# Base
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DEHYDRATED="${CURRENT_DIR}/dehydrated/dehydrated"
CONFIG="${CURRENT_DIR}/config.sh"
HOOK="${CURRENT_DIR}/hook.py"

# Normal usage
$DEHYDRATED -c -f $CONFIG -k $HOOK

# Cleanup unused certs
$DEHYDRATED -gc -f $CONFIG
