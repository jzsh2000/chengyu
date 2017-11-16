#!/usr/bin/env bash

cat chengyu.baidu.txt \
    | awk 'length($2) >= 9{print $1}' \
    | sort \
    > chengyu.1m.txt

cat chengyu.baidu.txt \
    | awk 'length($2) >= 10{print $1}' \
    | sort \
    > chengyu.10m.txt
