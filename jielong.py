#!/usr/bin/env python2
#-*- coding:utf-8 -*-
'''
chengyu jielong
'''

import random
import feather

chengyu_df = feather.read_dataframe('database/chengyu.feather')
with open('database/chengyu.start.3.txt') as f:
    chengyu_start = f.readlines()

chengyu_cur = random.choice(chengyu_start).strip().decode('utf-8')
chengyu_cur_dat = chengyu_df[chengyu_df.chengyu == chengyu_cur]

chengyu_cur_tail = chengyu_cur_dat.pinyin_tail2.values[0]
chengyu_cur_pinyin = chengyu_cur_dat.pinyin.values[0]

print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'

while True:
    chengyu_user = raw_input().strip().decode('utf-8')
    chengyu_user_dat = chengyu_df[chengyu_df.chengyu == chengyu_user]
    if chengyu_user_dat.shape[0] < 1:
        print '*** Game Over! ***'
        break
    elif chengyu_user_dat.pinyin_head2.values[0] != chengyu_cur_tail:
        print '+++ Game Over! +++'
        break
    else:
        chengyu_user_tail = chengyu_user_dat.pinyin_tail2.values[0]
        chengyu_cur_dat = chengyu_df[(chengyu_df.pinyin_head2 == chengyu_user_tail) &
                                     (chengyu_df.popular)]
        if chengyu_cur_dat.shape[0] < 1:
            print '--- You Win! ---'
            break
        else:
            chengyu_cur_dat = chengyu_cur_dat.sort_values('n', ascending=False).iloc[0]
            chengyu_cur = chengyu_cur_dat.chengyu
            chengyu_cur_pinyin = chengyu_cur_dat.pinyin
            chengyu_cur_tail = chengyu_cur_dat.pinyin_tail2
            print chengyu_cur + ' [' + chengyu_cur_pinyin + ']'
