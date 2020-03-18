import datetime
import http
import uuid
from urllib.parse import urlencode

import requests

import xixiang


class XiXiang:

    MENU_TYPE_LUNCH = "2"
    MENU_TYPE_DINNER = "4"
    ORDER_SUCCESS = "2"

    @classmethod
    def login(cls, phone, password, openid=None):
        """
        :rtype: XiXiang
        """
        openid = openid or uuid.uuid4().hex
        response = requests.post(xixiang.urls.login_url, data={"phone": phone, "password": password, "openid": openid})
        if response.status_code == http.HTTPStatus.OK.value:
            data = response.json()
            if data["code"] == 1:
                return cls(data["data"]["api_token"])
            else:
                raise xixiang.XiXiangLoginFail("{} 登录失败：{}".format(phone, data["message"]))
        elif response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY.value:
            raise xixiang.XiXiangLoginFail("{} 登录失败：密码错误".format(phone))
        raise xixiang.XiXiangLoginFail("{} 登录失败：服务器返回码 {}".format(phone, response.status_code))

    def __init__(self, api_token):
        self.api_token = api_token
        self.company_id = None
        self.menu_date = None

    def get_companies(self):
        companies = self.get(xixiang.urls.list_company_url)
        self.company_id = companies[0]["company_id"]
        return companies

    def get_menus(self):
        self.menu_date = str(datetime.date.today())
        if not self.company_id:
            self.get_companies()
        return xixiang.Menu.load(self.get(xixiang.urls.list_menu_url))

    def get_businesses(self, menu):
        return xixiang.Business.load(self.get(xixiang.urls.list_url, {"mt": menu.menu_type}))

    def get_items(self, business, menu):
        """
        :type business: xixiang.models.Business
        :type menu: xixiang.models.Menu
        """
        return xixiang.Item.load(
            self.get(xixiang.urls.cookbook_url, {"busid": business.business_id, "mt": menu.menu_type})
        )

    def add_item(self, item, num=1):
        """
        :type item: xixiang.models.Item
        :type num: int
        """
        return self.post(
            xixiang.urls.cart_add_url,
            json={
                "id": item.item_id,
                "menu_id": item.menu_id,
                "mt": item.menu_type,
                "num": num,
                "reserve_date": str(datetime.date.today()),
            },
        )

    def get_addresses(self):
        return xixiang.Address.load(self.get(xixiang.urls.user_address_url))

    def add_order(self, address, menu):
        return self.post(
            xixiang.urls.order_add_url,
            params={
                "menuType": menu.menu_type,
                "reserveDate": str(datetime.date.today()),
                "companyId": self.company_id,
            },
            data={"address_id": address.address_id},
        )

    def get_orders(self, status="", page=1):
        return self.get(xixiang.urls.order_list_url, params={"orderStatus": status, "page": page})

    def get(self, url, params=None):
        """
        :rtype: dict
        """
        url = self._prepare_url(url, params)
        response = requests.get(url)
        data = response.json()
        if data["code"] == 1:
            return data["data"]
        raise xixiang.XiXiangRequestError("请求失败：{}".format(data["message"]))

    def post(self, url, *, params=None, data=None, json=None):
        """
        :rtype: dict
        """
        url = self._prepare_url(url, params)
        response = requests.post(url, data=data, json=json)
        data = response.json()
        if data["code"] == 1:
            return data["data"]
        raise xixiang.XiXiangRequestError("请求失败：{}".format(data["message"]))

    def _prepare_url(self, url, params):
        if params is None:
            params = {}
        if self.company_id:
            params.setdefault("companyId", self.company_id)
        if self.menu_date:
            params.setdefault("menu_date", self.menu_date)
        params["api_token"] = self.api_token
        return "{}?{}".format(url, urlencode(sorted(params.items())))
