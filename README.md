成语接龙
========

配置运行环境
------------

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

使用脚本
--------

```bash
source venv/bin/activate
python jielong.py -a -t 0 -s 礼尚往来
```

示例输出：
```
礼尚往来 [lǐ shàng wǎng lái]
来之不易 [lái zhī bù yì]
易如反掌 [yì rú fǎn zhǎng]
掌上明珠 [zhǎng shàng míng zhū]
珠联璧合 [zhū lián bì hé]
合二为一 [hé èr wéi yī]
一目了然 [yī mù liǎo rán]
```

参数说明
--------

* `-a` - 自动继续成语接龙，直到找不到可用且未出现过的成语
* `-t` - 成语接龙类型，可取的值为：
    * [0]: 前一个成语最后一个字与后一个成语第一个字相同
    * [1]: 前一个成语最后一个字与后一个成语第一个字读音相同
    * [2]: 前一个成语最后一个字与后一个成语第一个字读音相近（音调可不同）
* `-s` - 指定第一个成语，如果该成语未出现在数据库中，则会报错退出
