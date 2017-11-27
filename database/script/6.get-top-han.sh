#!/usr/bin/env bash

cat db.txt \
    | cut -f1 \
    | grep -oP '\p{Han}' \
    | sort \
    | uniq -c \
    | sort -k1,1nr \
    | head 
