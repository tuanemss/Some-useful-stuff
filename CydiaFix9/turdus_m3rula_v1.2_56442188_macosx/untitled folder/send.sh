#!/usr/bin/env bash

echo "send pwnediBSS"

./checkm8_bootkit boot pwnediBSS

echo "send pwnediBEC"

./irecovery -f ibec.img3