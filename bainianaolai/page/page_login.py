from bainianaolai import page
from bainianaolai.base.base_bainianaolai import BaseBaiNianAoLai


class PageLogin(BaseBaiNianAoLai):
    # 我的
    def page_wode(self):
        self.base_click(page.test_wode)

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
    def page_click_login(self):
        self.base_click(page.test_click_login)

    def page_setting(self):
        self.base_click(page.test_setting)

    # 退出
    def page_loginout(self):
        self.base_click(page.test_loginout)

    # 确认
    def page_yes(self):
        self.base_click(page.test_yes)