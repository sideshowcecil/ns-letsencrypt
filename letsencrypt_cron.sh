#!/bin/bash

# normal usage
./dehydrated/dehydrated --config ./config.sh --hook ./hook.py --cron

# cleanup unused certs
./dehydrated/dehydrated --config ./config.sh --cleanup

