# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def get_url(*parts):
    return '{}/{}/'.format(base, '/'.join(parts))


protocol = 'http'

domain = 'api.platform.xixiang000.com'

base = '{}://{}'.format(protocol, domain)

login_url = get_url('login')

list_menu_url = get_url('list', 'getMenu')

list_url = get_url('list')

cookbook_url = get_url('cookbook')

cart_add_url = get_url('cart', 'add')

user_address_url = get_url('userAddress')

order_add_url = get_url('order', 'add')
