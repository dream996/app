import os
import sys

import allure

sys.path.append(os.getcwd())

from bainianaolai.read_yaml.read_yaml import read_yaml

import time

from bainianaolai.page.page_in import PageIn
import pytest
from selenium.webdriver.common.by import By


# 修饰类时,里面的函数执行之前,都会运行工厂函数
# @pytest.mark.usefixtures("putong")
class TestBaiNianAoLai:

    # 类级别  一个类开始结束都只执行一次
    def setup(self):
        self.bainianaolai = PageIn()

    def teardown(self):
        self.bainianaolai.driver.quit()

    # 普通函数修饰成工厂函数
    # 3.变成类函数  类似setup函数
    @pytest.fixture(scope="class", autouse=True)
    # 工厂函数以参数传递
    # @pytest.fixture()
    def putong(self):
        print("普通函数变成工厂函数")
        return 2

    # 1.以参数的形式传递
    # @pytest.mark.run(order=3)
    # @pytest.mark.xfail(2 > 1, reason="条件成立,不通过")
    def test_canshu(self, putong):
        print("fixturn以参数传递")

    # 过资源
    # 执行顺序
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    # @pytest.mark.skipif(putong(self=putong) == 2, reason="条件成立,跳过此用例")
    @allure.step("浏览分类资源")
    def test_fenlei(self):
        allure.attach("关闭弹窗", "")
        self.bainianaolai.page_fenlei().page_click_close()
        # 分类
        allure.attach("点击分类", "")
        self.bainianaolai.page_fenlei().page_click_fenlei()
        time.sleep(2)
        # 滑动
        allure.attach("浏览网页", "")
        for i in range(5):
            self.bainianaolai.page_fenlei().page_swipe()
        print("资源执行成功")

    # 登录退出流程
    # 执行顺序
    # 严重级别
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step("登录退出流程")
    @pytest.mark.run(order=2)
    # 2.以函数来传递
    # @pytest.mark.usefixtures("putong")
    @pytest.mark.parametrize("username,pwd", read_yaml())
    def test_login(self, username, pwd):
        # 断言用例是否能执行成功
        try:
            allure.attach("关闭弹窗", "")
            self.bainianaolai.page_fenlei().page_click_close()
            allure.attach("点击我的", "")
            self.bainianaolai.page_login().page_wode()
            allure.attach("已有账号登录", "")
            self.bainianaolai.page_login().page_you_zhanhao()
            # 断言用户名密码是否能登录成功
            allure.attach("开始断言", "")
            try:
                allure.attach("输入用户名和密码,点击登录", "")
                self.bainianaolai.page_login().page_name(username)
                self.bainianaolai.page_login().page_pwd(pwd)
                time.sleep(2)
                self.bainianaolai.page_login().page_click_login()
                old_text = "lq_0615142539_osc"
                new_text = By.ID, "com.yunmall.lc:id/tv_user_nikename"
                text = self.bainianaolai.page_login().base_find_element(new_text).text
                assert old_text == text
                print("登录成功")
            except:
                print("登录失败")
                imgname = "失败截图_{}.png".format(time.strftime("%Y%m%d%H%M%S"))
                self.bainianaolai.driver.get_screenshot_as_file(imgname)
                raise
            allure.attach("点击设置", "")
            self.bainianaolai.page_login().page_setting()
            allure.attach("屏幕滑到最底", "")
            self.bainianaolai.page_fenlei().page_swipe()
            allure.attach("退出账户", "")
            self.bainianaolai.page_login().page_loginout()
            allure.attach("点击确认", "")
            self.bainianaolai.page_login().page_yes()
        except:
            allure.attach("用例执行失败截图", "")
            print("用例执行失败")
            img = "用例执行失败_{}.png".format(time.strftime("%Y%m%d%H%M%S"))
            self.bainianaolai.driver.get_screenshot_as_file(img)
            raise
        else:
            print("用例执行成功")
