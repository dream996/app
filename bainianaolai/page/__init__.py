from selenium.webdriver.common.by import By

# 关闭弹窗
test__click_close = By.ID, "com.yunmall.lc:id/img_close"
# 分类
test_fenlei = By.ID, "com.yunmall.lc:id/tab_category"
# 家居
test_jiaju = By.CLASS_NAME, "android.widget.TextView"
# 我的
test_wode = By.ID, "com.yunmall.lc:id/tab_me"
# 手机注册
test_shouji_zhuce = By.ID, "com.yunmall.lc:id/register_button"
# 输入手机
test_tel = By.ID, "com.yunmall.lc:id/register_phone_textview"
# 已有账号去登陆
test_you_zhanhao = By.ID, "com.yunmall.lc:id/textView1"
# 输入账号
test_name = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
test_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录
test_login = By.ID, "com.yunmall.lc:id/logon_button"
# 点击设置
test_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 点击退出
test_loginout = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认
test_yes = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
# toast
message='//*[@text="登录密码错误"]'
test_toast=By.XPATH,message