# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class XiXiangError(Exception):
    """ XiXiang 包产生的错误 """


class XiXiangRequestError(XiXiangError):
    """ 网络请求过程中的一些错，比如状态码不是200，code不是1 """


class XiXiangLoginFail(XiXiangError):
    """ 用户名或密码错误，导致的登录失败 """
