#!/bin/bash

# force renewal
./dehydrated/dehydrated --config ./config.sh --hook ./hook.py --cron --force

# cleanup unused certs
./dehydrated/dehydrated --config ./config.sh --cleanup

