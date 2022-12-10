from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


#创建对象库层  git
class IndexPage(BasePage):
    #初始化驱动对象

    def __init__(self):
        super().__init__()
        #定义元素的定位信息：定位策略，定位依据
        self.login_button = [By.CSS_SELECTOR,'.red']

    #定义元素，并返回元素
    def find_login_button(self):
        return self.base_find_element(self.login_button)

#创建操作层
class IndexHandle(BaseHandle):
    #创建对象库层对象
    def __init__(self):
        self.index_page = IndexPage()

    #定义点击登陆按钮的方法
    def click_login_button(self):
        self.index_page.find_login_button().click()

#创建业务层
class IndexProxy:
    #创建操作层对象
    def __init__(self):
        self.inde_handle = IndexHandle()

    #定义点击登陆按钮的业务
    def click_login_button(self):
        self.inde_handle.click_login_button()