#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
chengyu jielong
'''

import random
import argparse
import feather

parser = argparse.ArgumentParser(description='chengyu jielong')
parser.add_argument('-a', '--auto',
                    help='auto continue jielong',
                    action='store_true')
parser.add_argument('-t', '--type',
                    help='jielong type',
                    type=int, choices=[0, 1, 2], default=2)
args = parser.parse_args()

chengyu_df = feather.read_dataframe('database/chengyu.feather')
with open('database/chengyu.start.3.txt') as f:
    chengyu_start = f.readlines()

if args.type == 0:
    head_column = 'chengyu_head'
    tail_column = 'chengyu_tail'
elif args.type == 1:
    head_column = 'pinyin_head'
    tail_column = 'pinyin_tail'
else:
    head_column = 'pinyin_head2'
    tail_column = 'pinyin_tail2'

chengyu_cur = random.choice(chengyu_start).strip().decode('utf-8')
chengyu_cur_dat = chengyu_df[chengyu_df.chengyu == chengyu_cur]

chengyu_cur_tail = chengyu_cur_dat[tail_column].values[0]
chengyu_cur_pinyin = chengyu_cur_dat.pinyin.values[0]

print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'
chengyu_history = [chengyu_cur]

if args.auto:
    while True:
        chengyu_cur_dat = chengyu_df[(chengyu_df[head_column] == chengyu_cur_tail) &
                                     (chengyu_df.popular)]

        if chengyu_cur_dat.shape[0] < 1:
            break

        chengyu_cur_dat = chengyu_cur_dat.sort_values('n', ascending=False)
        chengyu_flag = False
        for i in xrange(chengyu_cur_dat.shape[0]):
            chengyu_cur = chengyu_cur_dat.iloc[i].chengyu
            if chengyu_cur not in chengyu_history:
                chengyu_flag = True
                chengyu_cur_dat = chengyu_cur_dat.iloc[i]
                break

        if chengyu_flag:
            chengyu_history.append(chengyu_cur)
            chengyu_cur_pinyin = chengyu_cur_dat.pinyin
            chengyu_cur_tail = chengyu_cur_dat[tail_column]
            print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'
        else:
            break
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
