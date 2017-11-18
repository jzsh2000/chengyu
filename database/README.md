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

* `chengyu.txt` - 所有的成语列表
* `chengyu.baidu.txt` -  所有的成语列表及其在百度中的搜索结果数
* `chengyu.1m.txt` - 百度搜索结果超过 1M 条的成语
* `chengyu.10m.txt` - 百度搜索结果超过 10M 条的成语
* `chengyu.feather` - 整理后的成语信息，可以被 R 或 python 导入

以下文件保存在本地，不在 git 仓库中:

* `db.txt` - 所有成语，包括拼音和释义
* `db.err.txt` - 抓取出错的成语列表（目前只有*五湖四海*）
