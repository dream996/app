from bainianaolai import page
from bainianaolai.base.base_bainianaolai import BaseBaiNianAoLai


class PageFenlei(BaseBaiNianAoLai):
    # 点击关闭
    def page_click_close(self):
        self.base_click(page.test__click_close)

    # 分类
    def page_click_fenlei(self):
        self.base_click(page.test_click_fenlei)

    # 默认家居家纺,从上到下浏览网页
    def page_swipe(self):
        self.base_swipe()

    # 手机号注册
    def page_shouji_zhuce(self):
        self.base_click(page.test_shouji_zhuce)

    # 输入手机号
    def page_tel(self, values="18571772032"):
        self.base_input(page.test_tel, values)