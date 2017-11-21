#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
chengyu jielong
'''

import random
import feather
import pandas as pd

chengyu_df = feather.read_dataframe('database/chengyu.feather')
with open('database/chengyu.start.3.txt') as f:
    chengyu_start = f.readlines()

print random.choice(chengyu_start).strip()