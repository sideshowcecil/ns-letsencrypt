#!/bin/bash

# normal usage
./dehydrated/dehydrated -c -f ./config.sh -k ./hook.py

# cleanup unused certs
./dehydrated/dehydrated -gc -f ./config.sh

