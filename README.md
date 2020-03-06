# XiXiang 熙香点餐
[![PyPI](https://img.shields.io/pypi/v/xixiang.svg)](https://pypi.python.org/pypi/xixiang)
[![Build](https://github.com/LKI/xixiang/workflows/Build/badge.svg)](https://github.com/LKI/xixiang)

> 支持 Python 3.5+ 的熙香点餐非官方库


## 背景

因为[我司](https://www.lagou.com/gongsi/j86312.html)点餐的人比较多，
~~想着加一个点餐服务做灾备，~~
于是就除了[美餐](https://github.com/LKI/meican)我们还得支持熙香点餐。


## 安装

```bash
pip install xixiang
```


## 代码调用

```python
import xixiang

try:
    client = xixiang.XiXiang.login("1881881888", "hunter2")
    menus = client.get_menus()
    shops = client.get_businesses(menus[0])
    dishes = client.get_items(shops[0], menus[0])
    if any(dish for dish in dishes if dish.menu_name == "香酥鸡腿"):
        print("今天有香酥鸡腿 :happy:")
    else:
        print("今天没有香酥鸡腿 :sad:")
except xixiang.XiXiangError as ex:
    print("Error: {}".format(ex))
```


## 贡献

不论是任何疑问、想要的功能~~还是想吃的套餐~~都欢迎[直接提 issue](https://github.com/LKI/xixiang/issues/new)

假如你们公司是用美餐点餐的，
[隔壁也有美餐的库噢~](https://github.com/LKI/meican)

:wink: 欢迎各种 PR


## 协议

宽松的 [MIT](https://github.com/LKI/xixiang/blob/master/LICENSE) 协议：

- ✔ 支持各种改写
- ✔ 支持你把代码作者都改成自己
- ✖ 不支持每天中午免费吃西贝莜面村
- ✖ 也不支持点大羊腿、掌中宝
