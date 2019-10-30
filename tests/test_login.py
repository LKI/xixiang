import http
import unittest

import requests_mock

import xixiang
from xixiang.urls import login_url


class LoginTests(unittest.TestCase):
    def test_login_fail(self):
        with self.assertRaises(xixiang.XiXiangError), requests_mock.mock() as mocker:
            mocker.post(login_url, status_code=http.HTTPStatus.UNPROCESSABLE_ENTITY.value)
            xixiang.XiXiang.login("12345678910", "123456")
