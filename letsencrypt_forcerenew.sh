#!/bin/bash

# Base
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DEHYDRATED="${CURRENT_DIR}/dehydrated/dehydrated"
CONFIG="${CURRENT_DIR}/config.sh"
HOOK="${CURRENT_DIR}/hook.py"

# Force renewal
$DEHYDRATED -c -f $CONFIG -x -k $HOOK

# Cleanup unused certs
$DEHYDRATED -gc -f $CONFIG
