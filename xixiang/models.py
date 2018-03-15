# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Model(object):
    @classmethod
    def load(cls, data):
        pass


class Menu(Model):
    def __init__(self, name, menu_type):
        self.name = name
        self.menu_type = menu_type

    @classmethod
    def load(cls, data):
        """
        :rtype: list[Menu]
        """
        menus = []
        for menu_type, name in data.items():
            menus.append(cls(name, menu_type))
        return menus

    def __repr__(self):
        return '{} {}'.format(self.menu_type, self.name)


class Business(Model):
    def __init__(self, data):
        self.business_id = data['business_id']
        self.business_name = data['business_name']
        self.company_id = data['company_id']
        self.raw_data = data

    @classmethod
    def load(cls, instances):
        """
        :rtype: list[Business]
        """
        businesses = []
        for data in instances:
            businesses.append(cls(data))
        return businesses

    def __repr__(self):
        return '{} {}'.format(self.business_id, self.business_name)


class Item(Model):
    def __init__(self, data):
        self.item_id = data['id']
        self.menu_id = data['menu_id']
        self.menu_type = data['menu_type']
        self.is_sell = bool(data['is_sell'])
        self.menu_name = data['cookbook']['menu_name']
        self.raw_data = data

    @classmethod
    def load(cls, data):
        """
        :rtype: list[Item]
        """
        businesses = []
        for items_data in data.values():
            for item_data in items_data:
                businesses.append(cls(item_data))
        return businesses

    def __repr__(self):
        return '{} {}'.format(self.item_id, self.menu_name)


class Address(Model):
    def __init__(self, data):
        self.address_id = data['id']
        self.address = data['consignee_address']
        self.raw_data = data

    @classmethod
    def load(cls, instances):
        """
        :rtype: list[Address]
        """
        addresses = []
        for instance in instances:
            addresses.append(cls(instance))
        return addresses

    def __repr__(self):
        return '{} {}'.format(self.address_id, self.address)
