import os
import sys

import pytest

sys.path.append(os.getcwd())
import time

from selenium.webdriver.common.by import By


from bainianaolai.base.get_driver import get_driver
from bainianaolai.page.page_bainianaolai import PageBaiNianAoLai

# 修饰类时,里面的函数执行之前,都会运行工厂函数
# @pytest.mark.usefixtures("putong")
class TestBaiNianAoLai:

    # 类级别  一个类开始结束都只执行一次
    def setup(self):
        self.driver = get_driver()
        self.bainianaolai = PageBaiNianAoLai(self.driver)

    def teardown(self):
        self.bainianaolai.driver.quit()

    # 普通函数修饰成工厂函数
    # 3.变成类函数  类似setup函数
    @pytest.fixture(scope="class",autouse=True)
    def putong(self):
        print("普通函数变成工厂函数")

    # 1.以参数的形式传递
    @pytest.mark.run(order=3)
    def test_canshu(self,putong):
        print("以参数传递")

    # 执行顺序
    @pytest.mark.run(order=1)
    def test_fenlei(self):
        self.bainianaolai.page_click_close()
        # 分类
        self.bainianaolai.page_fenlei()
        time.sleep(2)
        # 滑动
        for i in range(5):
            self.bainianaolai.page_swipe()
        print("资源执行成功")

    # 登录退出流程
    # 执行顺序
    @pytest.mark.run(order=2)
    # 2.以函数来传递
    # @pytest.mark.usefixtures("putong")
    def test_login(self,name="18571772032", pwd="123456"):
        # 断言用例是否能执行成功
        try:
            self.bainianaolai.page_click_close()
            self.bainianaolai.page_wode()
            self.bainianaolai.page_you_zhanhao()
            # 断言用户名密码是否能登录成功
            try:
                self.bainianaolai.page_name(name)
                self.bainianaolai.page_pwd(pwd)
                self.bainianaolai.page_login()
                old_text = "lq_0615142539_osc"
                new_text = By.ID, "com.yunmall.lc:id/tv_user_nikename"
                text = self.bainianaolai.base_find_element(new_text).text
                assert old_text == text
                print("登录成功")
            except:
                print("登录失败")
                img = "失败截图_{}.png".format(time.strftime("%Y%m%d%H%M%S"))
                self.driver.get_screenshot_as_file(img)
                raise
            self.bainianaolai.page_setting()
            self.bainianaolai.page_swipe()
            self.bainianaolai.page_loginout()
            self.bainianaolai.page_yes()
        except:
            print("用例执行失败")
            img = "用例执行失败_{}.png".format(time.strftime("%Y%m%d%H%M%S"))
            self.driver.get_screenshot_as_file(img)
            raise
        else:
            print("用例执行成功")