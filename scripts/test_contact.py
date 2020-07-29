import allure
from appium import webdriver
import pytest


class TestContact:

    @allure.severity("CRITICAL")
    @allure.step(title="登录的测试脚本")
    def test_login(self):
        allure.attach("输入密码", "输入密码的描述")
        print("输入密码")
        allure.attach("点击登录", "点击登录的描述")
        print("点击登录")
        # print("123")
        assert 1

    @allure.severity("CRITICAL")
    @allure.step(title="用户名的测试脚本")
    def test_username(self):
        # print("123")
        assert 1

    @allure.severity("TRIVIAL")
    @allure.step(title="密码的测试脚本")
    def test_password(self):
        # print("123")
        assert 1
