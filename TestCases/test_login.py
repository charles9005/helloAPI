"""
=============================
@Time: 2022-6-15 20:55
@Author: Charles Lin
@Email: 626853099@qq.com
@File: test_login.py
@Company: CATL
=============================
"""
import allure

@allure.story("测试登录")
class TestLogin:
    @allure.title("登录成功")
    def test_login_success(self):
        pass

    @allure.title("登录失败")
    def test_login_failed(self):
        pass

