#!/bin/bash

BASE_URL="http://cydia.vn"
OUTPUT_DIR="$HOME/debs"

mkdir -p "$OUTPUT_DIR"

while IFS= read -r line; do
  if [[ "$line" == Filename:* ]]; then
    FILE_PATH="${line#Filename: }"
    FULL_PATH="$OUTPUT_DIR/$FILE_PATH"
    DIR_PATH=$(dirname "$FULL_PATH")

    mkdir -p "$DIR_PATH"
    echo " Download: $FILE_PATH"
    curl -s -o "$FULL_PATH" "$BASE_URL/$FILE_PATH"
  fi
done < Packages
