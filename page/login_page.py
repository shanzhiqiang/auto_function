from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


#创建对象库层
class LoginPage(BasePage):
    #初始化驱动对象
    def __init__(self):
        super().__init__()
        #定义元素的定位信息：定位策略，定位依据
        self.username = [By.NAME,'username']
        self.password = [By.NAME,'password']
        self.code = [By.NAME,'verify_code']
        self.button = [By.NAME,'sbtbutton']

    #定义定位元素的方法，并返回元素
    def find_username(self):
        return self.base_find_element(self.username)

    def find_password(self):
        return self.base_find_element(self.password)

    def find_code(self):
        return self.base_find_element(self.code)

    def find_button(self):
        return self.base_find_element(self.button)

#创建操作层
class LoginHandle(BaseHandle):
    #创建对象库层对象
    def __init__(self):
        self.login_page = LoginPage()

    #定义用户名输入的操作
    def input_username(self,text):
        self.base_input_text(self.login_page.find_username(),text)

    #定义密码的输入操作
    def input_password(self,text):
        self.base_input_text(self.login_page.find_password(),text)

    #定义验证码的输入操作
    def input_code(self,text):
        self.base_input_text(self.login_page.find_code(),text)

    #定义登录按钮的点击操作
    def click_button(self):
        self.login_page.find_button().click()


#创建业务层
class LoginProxy:
    #创建操作层对象
    def __init__(self):
        self.login_handle = LoginHandle()

    #定义登录操作
    def login(self,username,password,code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_code(code)
        self.login_handle.click_button()
