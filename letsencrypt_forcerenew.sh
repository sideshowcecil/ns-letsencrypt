#!/bin/bash

# force renewal
./dehydrated/dehydrated -c -f ./config.sh -x -k ./hook.py

# cleanup unused certs
./dehydrated/dehydrated -gc -f $./config.sh

