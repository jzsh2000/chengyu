#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
chengyu jielong
'''

import sys
import random
import argparse
import feather
import numpy as np
from numpy.random import choice

parser = argparse.ArgumentParser(description='chengyu jielong')
parser.add_argument('-a', '--auto',
                    help='auto continue jielong',
                    action='store_true')
parser.add_argument('-t', '--type',
                    help='jielong type',
                    type=int, choices=[0, 1, 2], default=2)
parser.add_argument('-s', '--start',
                    help='define the first chengyu',
                    default='')
args = parser.parse_args()

if args.type == 0:
    chengyu_start_file = 'database/chengyu.start.1.txt'
    head_column = 'chengyu_head'
    tail_column = 'chengyu_tail'
elif args.type == 1:
    chengyu_start_file = 'database/chengyu.start.2.txt'
    head_column = 'pinyin_head'
    tail_column = 'pinyin_tail'
else:
    chengyu_start_file = 'database/chengyu.start.3.txt'
    head_column = 'pinyin_head2'
    tail_column = 'pinyin_tail2'

chengyu_df = feather.read_dataframe('database/chengyu.feather')
with open(chengyu_start_file) as f:
    chengyu_start = f.readlines()

if args.start != '':
    chengyu_cur = args.start.strip().decode('utf-8')
    chengyu_cur_dat = chengyu_df[chengyu_df.chengyu == chengyu_cur]
    if chengyu_cur_dat.shape[0] < 1:
        print 'Error: chengyu not in database'
        sys.exit(1)
else:
    chengyu_cur = random.choice(chengyu_start).strip().decode('utf-8')
    chengyu_cur_dat = chengyu_df[chengyu_df.chengyu == chengyu_cur]

chengyu_cur_tail = chengyu_cur_dat[tail_column].values[0]
chengyu_cur_pinyin = chengyu_cur_dat.pinyin.values[0]

print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'
chengyu_history = [chengyu_cur]

if args.auto:
    while True:
        chengyu_cur_dat = chengyu_df[(chengyu_df[head_column] == chengyu_cur_tail) &
                                     (chengyu_df.popular) &
                                     (~chengyu_df.chengyu.isin(chengyu_history))]

        if chengyu_cur_dat.shape[0] < 1:
            break

        # chengyu_cur_dat = chengyu_cur_dat.sort_values('n', ascending=False)
        chengyu_p = chengyu_cur_dat.n.values
        chengyu_p = np.array(chengyu_p) / (np.sum(chengyu_p) + .0)
        chengyu_iloc = choice(range(chengyu_cur_dat.shape[0]),
                              p=chengyu_p)
        chengyu_cur_dat = chengyu_cur_dat.iloc[chengyu_iloc]
        chengyu_cur = chengyu_cur_dat.chengyu

        chengyu_history.append(chengyu_cur)
        chengyu_cur_pinyin = chengyu_cur_dat.pinyin
        chengyu_cur_tail = chengyu_cur_dat[tail_column]
        print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'

else:
    while True:
        chengyu_user = raw_input().strip().decode('utf-8')
        chengyu_user_dat = chengyu_df[chengyu_df.chengyu == chengyu_user]
        if chengyu_user_dat.shape[0] < 1:
            print '*** Game Over! ***'
            break
        elif chengyu_user_dat[head_column].values[0] != chengyu_cur_tail:
            print '+++ Game Over! +++'
            break
        else:
            chengyu_user_tail = chengyu_user_dat[tail_column].values[0]
            chengyu_cur_dat = chengyu_df[(chengyu_df[head_column] == chengyu_user_tail) &
                                         (chengyu_df.popular)]
            if chengyu_cur_dat.shape[0] < 1:
                print '--- You Win! ---'
                break
            else:
                chengyu_cur_dat = chengyu_cur_dat.sort_values('n', ascending=False).iloc[0]
                chengyu_cur = chengyu_cur_dat.chengyu
                chengyu_cur_pinyin = chengyu_cur_dat.pinyin
                chengyu_cur_tail = chengyu_cur_dat[tail_column]
                print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'
