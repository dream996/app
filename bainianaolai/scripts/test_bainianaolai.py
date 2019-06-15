import os
import sys
import time

sys.path.append(os.getcwd())

import pytest

from bainianaolai.base.get_driver import get_driver
from bainianaolai.page.page_bainianaolai import PageBaiNianAoLai


class TestBaiNianAoLai:

    # 类级别  一个类开始结束都只执行一次
    def setup_class(self):
        self.driver = get_driver()
        self.bainianaolai = PageBaiNianAoLai(self.driver)

    def teardown_class(self):
        self.bainianaolai.driver.quit()

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
    def test_login(self,name="18571772032",pwd="123456"):
        self.bainianaolai.page_click_close()
        self.bainianaolai.page_wode()
        self.bainianaolai.page_you_zhanhao()
        self.bainianaolai.page_name(name)
        time.sleep(2)
        self.bainianaolai.page_pwd(pwd)
        self.bainianaolai.page_login()
        self.bainianaolai.page_setting()
        self.bainianaolai.page_swipe()
        self.bainianaolai.page_loginout()
        self.bainianaolai.page_yes()