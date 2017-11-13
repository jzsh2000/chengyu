#!/usr/bin/env bash

cat db.err.txt db.txt \
    | awk 'length($1) == 12{print $1}' \
    | sort \
    > chengyu.txt
