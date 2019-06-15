from selenium.webdriver.common.by import By

from bainianaolai.base.base_bainianaolai import BaseBaiNianAoLai


class PageBaiNianAoLai(BaseBaiNianAoLai):
    test__click_close=By.ID,"com.yunmall.lc:id/img_close"
    test_fenlei=By.ID,"com.yunmall.lc:id/tab_category"
    test_jiaju=By.CLASS_NAME,"android.widget.TextView"

    def page_click_close(self):
        self.base_click(self.test__click_close)

    # 分类
    def page_fenlei(self):
        self.base_click(self.test_fenlei)

    # 默认家居家纺,从上到下浏览网页
    def page_jiaju(self):
        self.base_swipe()