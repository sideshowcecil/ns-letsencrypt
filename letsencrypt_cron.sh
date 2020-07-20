#!/bin/bash

# normal usage
./dehydrated/dehydrated -c -f ./config.sh -k ./hookpy

# cleanup unused certs
./dehydrated/dehydrated -gc -f ./config.sh

