import os
import sys
import time

import pytest
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from bainianaolai.base.get_driver import get_driver
from bainianaolai.page.page_bainianaolai import PageBaiNianAoLai


class TestBaiNianAoLai:

    # 类级别  一个类开始结束都只执行一次
    def setup(self):
        self.driver = get_driver()
        self.bainianaolai = PageBaiNianAoLai(self.driver)

    def teardown(self):
        self.bainianaolai.driver.quit()

    @pytest.mark.run(order=2)
    def test_bainianaolai(self):
        self.bainianaolai.page_click_close()
        # 分类
        self.bainianaolai.page_fenlei()
        time.sleep(2)
        # 滑动
        for i in range(5):
            self.bainianaolai.page_swipe()
        time.sleep(2)

    # 登录退出流程
    @pytest.mark.run(order=1)
    def test_login(self, name="18571772032", pwd="123456"):
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