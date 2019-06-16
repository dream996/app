from bainianaolai.base.get_driver import get_driver
from bainianaolai.page.page_fenlei import PageFenlei

from bainianaolai.page.page_login import PageLogin


# 统一入口类
class PageIn():
    # 获取driver
    def __init__(self):
        self.driver=get_driver()

    # 获取分类页面方法
    def page_fenlei(self):
        return PageFenlei(self.driver)

    # 获取登录页面方法
    def page_login(self):
        return PageLogin(self.driver)