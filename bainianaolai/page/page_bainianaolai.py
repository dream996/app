from bainianaolai import page
from bainianaolai.base.base_bainianaolai import BaseBaiNianAoLai


class PageBaiNianAoLai(BaseBaiNianAoLai):
    # 点击关闭
    def page_click_close(self):
        self.base_click(page.test__click_close)

    # 分类
    def page_fenlei(self):
        self.base_click(page.test_fenlei)

    # 默认家居家纺,从上到下浏览网页
    def page_swipe(self):
        self.base_swipe()

    # 我的
    def page_wode(self):
        self.base_click(page.test_wode)

    # 手机号注册
    def page_shouji_zhuce(self):
        self.base_click(page.test_shouji_zhuce)

    # 输入手机号
    def page_tel(self, values="18571772032"):
        self.base_input(page.test_tel, values)

    # 已有账号去登陆
    def page_you_zhanhao(self):
        self.base_click(page.test_you_zhanhao)

    # 输入用户名
    def page_name(self, name):
        self.base_input(page.test_name, name)

    # 密码
    def page_pwd(self, pwd):
        self.base_input(page.test_pwd, pwd)

    # 点击登录
    def page_login(self):
        self.base_click(page.test_login)

    def page_setting(self):
        self.base_click(page.test_setting)

    # 退出
    def page_loginout(self):
        self.base_click(page.test_loginout)

    # 确认
    def page_yes(self):
        self.base_click(page.test_yes)