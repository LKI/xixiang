# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import http

import requests
import six

import xixiang


class XiXiang(object):
    @classmethod
    def login(cls, phone, password):
        """
        :rtype: XiXiang
        """
        response = requests.post(xixiang.urls.login_url, {'phone': phone, 'password': password})
        if response.status_code == http.HTTPStatus.OK.value:
            data = response.json()
            if data['code'] == 1:
                return cls(data['data'])
            else:
                raise xixiang.XiXiangLoginFail('{} 登录失败：{}'.format(phone, data['message']))
        elif response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY.value:
            raise xixiang.XiXiangLoginFail('{} 登录失败：密码错误'.format(phone))
        raise xixiang.XiXiangLoginFail('{} 登录失败：服务器返回码 {}'.format(phone, response.status_code))

    def __init__(self, api_token):
        self.api_token = api_token

    def get_menu(self):
        return self.get(xixiang.urls.list_menu_url)

    def get_list(self, mt):
        return self.get(xixiang.urls.list_url, {'mt': mt})

    def get_cookbook(self, busid, comid, mt):
        return self.get(xixiang.urls.cookbook_url, {'busid': busid, 'comid': comid, 'mt': mt})

    def add_item(self, item_id, menu_id, mt, num=1):
        return self.post(
            xixiang.urls.cart_add_url,
            {'id': item_id, 'menu_id': menu_id, 'mt': mt, 'num': num, 'reserve_date': 'undefined'},
        )

    def add_order(self, address_id):
        return self.post(xixiang.urls.order_add_url, {'address_id': address_id})

    def get(self, url, params=None):
        """
        :rtype: dict
        """
        if params is None:
            params = {}
        params['api_token'] = self.api_token
        url = '{}?{}'.format(url, six.moves.urllib.parse.urlencode(sorted(params.items())))
        response = requests.get(url)
        data = response.json()
        if data['code'] == 1:
            return data['data']
        raise xixiang.XiXiangRequestError('请求失败：{}'.format(data['message']))

    def post(self, url, data=None):
        """
        :rtype: dict
        """
        url = '{}?api_token={}'.format(url, self.api_token)
        response = requests.post(url, data or {})
        data = response.json()
        if data['code'] == 1:
            return data['data']
        raise xixiang.XiXiangRequestError('请求失败：{}'.format(data['message']))
