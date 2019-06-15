from selenium.webdriver.support.wait import WebDriverWait


class BaseBaiNianAoLai():

    # 获取driver
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 滑动
    def base_swipe(self):
        self.driver.swipe(838,2275,838,382,duration=2000)