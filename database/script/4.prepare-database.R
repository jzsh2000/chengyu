library(tidyverse)
library(stringr)
library(feather)

db <- read_tsv('db.txt', col_names = c('chengyu', 'pinyin'), col_types = 'cc_')
db = bind_rows(db,
               data_frame(
                   chengyu = '五湖四海',
                   pinyin = 'wǔ hú sì hǎi'
               )) %>%
    filter(str_length(chengyu) == 4) %>%
    arrange(chengyu) %>%
    mutate(pinyin = str_trim(pinyin)) %>%
    mutate(pinyin = str_replace_all(pinyin, '\\s+', ' ')) %>%
    filter(!str_detect(chengyu, fixed('?')))

db$pinyin[db$chengyu == '跌宕风流'] = 'diē dàng fēng liú'
db$pinyin[db$chengyu == '改行自新'] = 'gǎi xíng zì xīn'
db$pinyin[db$chengyu == '悬龟系鱼'] = 'xuán guī jì yú'
db$pinyin[db$chengyu == '抓耳搔腮'] = 'zhuā ěr sāo sāi'
db$pinyin[db$chengyu == '足尺加二'] = 'zú chǐ ji èr'

db$pinyin[db$chengyu == '丢魂丧胆'] = 'diū hún sàng dǎn'
db$pinyin[db$chengyu == '聪明才智'] = 'cōng míng cái zhì'
db$pinyin[db$chengyu == '蔽聪塞明'] = 'bì cōng sè míng'
db$pinyin[db$chengyu == '心烦技痒'] = 'xīn fán jì yǎng'

map_vowel <- function(x) {
    x = str_replace_all(x, '[āáǎà]', 'a')
    x = str_replace_all(x, '[ēéěè]', 'e')
    x = str_replace_all(x, '[īíǐì]', 'i')
    x = str_replace_all(x, '[ōóǒò]', 'o')
    x = str_replace_all(x, '[ūúǔù]', 'u')
    x = str_replace_all(x, '[üǖǘǚǜ]', 'v')
    str_to_lower(x)
}

db_full = db %>%
    mutate(chengyu_head = map_chr(chengyu, ~str_extract(., '^.')),
           chengyu_tail = map_chr(chengyu, ~str_extract(., '.$')),
           pinyin_head = str_split_fixed(pinyin, ' ', 4)[,1],
           pinyin_tail = str_split_fixed(pinyin, ' ', 4)[,4],
           pinyin_head2 = map_chr(pinyin_head, ~map_vowel(.)),
           pinyin_tail2 = map_chr(pinyin_tail, ~map_vowel(.)))

db_baidu <- read_delim('chengyu.baidu.txt', delim = ' ',
                       col_names = c('chengyu', 'n'),
                       col_types = 'cc') %>%
    mutate(n = as.integer(str_replace_all(n, ',', '')))

db_full_baidu = db_full %>%
    inner_join(db_baidu, by = 'chengyu') %>%
    mutate(rank = min_rank(desc(n)),
           popular = (n >= 1000000)) %>%
    arrange(chengyu)

write_feather(db_full_baidu, 'chengyu.feather')
