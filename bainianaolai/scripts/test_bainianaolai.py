import os
import sys
import time

sys.path.append(os.getcwd())

import pytest


from bainianaolai.base.get_driver import get_driver
from bainianaolai.page.page_bainianaolai import PageBaiNianAoLai


class TestBaiNianAoLai:

    def setup(self):
        self.driver=get_driver()
        self.bainianaolai=PageBaiNianAoLai(self.driver)

    def teardown(self):
        self.bainianaolai.driver.quit()

    def test_bainianaolai(self):
        self.bainianaolai.page_click_close()
        # 分类
        self.bainianaolai.page_fenlei()
        time.sleep(2)
        # 滑动
        for i in range(5):
            self.bainianaolai.page_jiaju()

        time.sleep(3)
if __name__ == '__main__':
    pytest.main("-s test_bainianaolai.py")