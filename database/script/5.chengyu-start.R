library(feather)
library(tidyverse)

db_full_baidu <- read_feather('chengyu.feather')
db_full_baidu_popular = db_full_baidu %>%
    filter(n >= 10000000)

# 出现比较多的成语第一个字
top_head = db_full_baidu_popular %>%
    count(chengyu_head, sort = TRUE) %>%
    filter(nn >= 5) %>%
    pull(chengyu_head)

# 出现比较多的成语第一个字的拼音（带音调）
top_head2 = db_full_baidu_popular %>%
    count(pinyin_head, sort = TRUE) %>%
    filter(nn >= 5) %>%
    pull(pinyin_head)

# 出现比较多的成语第一个字的拼音（不带音调）
top_head3 = db_full_baidu_popular %>%
    count(pinyin_head2, sort = TRUE) %>%
    filter(nn >= 5) %>%
    pull(pinyin_head2)

# ----- 获取成语接龙起始成语列表
db_full_baidu_popular %>%
    filter(chengyu_tail %in% top_head) %>%
    pull(chengyu) %>%
    write_lines('chengyu.start.1.txt')

db_full_baidu_popular %>%
    filter(pinyin_tail %in% top_head2) %>%
    pull(chengyu) %>%
    write_lines('chengyu.start.2.txt')

db_full_baidu_popular %>%
    filter(pinyin_tail2 %in% top_head3) %>%
    pull(chengyu) %>%
    write_lines('chengyu.start.3.txt')
