数据来源
========

<http://chengyu.t086.com/>


下载数据
========

```bash
python script/0.download.py
bash script/1.four-word.sh

python script/2.search_num.py chengyu.txt chengyu.baidu.txt
bash script/3.get-1m-chengyu.sh
```

详细内容
========

从网页抓取的数据:

* `db.txt` - 所有成语，包括拼音和释义
* `db.err.txt` - 抓取出错的成语列表（目前只有*五湖四海*）

本地处理后的数据:

* `chengyu.txt` - 所有的成语列表
* `chengyu.baidu.txt` -  所有的成语列表及其在百度中的搜索结果数
* `chengyu.1m.txt` - 百度搜索结果超过 1M 条的成语
* `chengyu.10m.txt` - 百度搜索结果超过 10M 条的成语
* `chengyu.start.1.txt` - 成语接龙起始成语 (要求首尾同字时)
* `chengyu.start.2.txt` - 成语接龙起始成语 (要求首尾同音时)
* `chengyu.start.3.txt` - 成语接龙起始成语 (要求首尾同音但可以不同调时)
* `chengyu.feather` - (二进制文件) 整理后的成语信息，可以被 R 或 python 导入

数据统计
========

所有成语共 30880 个（其中 1 个抓取失败），涉及到 4852 个汉字

* —— 其中四字成语共 29489 个
* ———— 其中百度搜索结果超过 1M 条的四字成语共 6554 个
* —————— 其中百度搜索结果超过 10M 条的四字成语共 2331 个

成语中出现次数最多的 10 个汉字如下（括号中的数字为出现的次数）：

1. 不 (2525)
2. 之 (1358)
3. 一 (1323)
4. 无 (1118)
5. 心 (970)
6. 人 (951)
7. 天 (770)
8. 风 (759)
9. 如 (596)
10. 大 (551)
