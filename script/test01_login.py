import time
import unittest
import logging

from parameterized import parameterized

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from tools.config import get_tips_info, get_data
from utils import DriverUtil


class TestLogin(unittest.TestCase):

    #初始化驱动对象
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        #创建业务层对象
        cls.index_proxy = IndexProxy()
        cls.login_proxy = LoginProxy()

    #销毁驱动对象
    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    #打开首页
    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1/')

    #等2秒
    def tearDown(self) -> None:
        time.sleep(2)

    #创建测试用例
    def test01_login_success(self):  #登录成功用例
        self.index_proxy.click_login_button()
        time.sleep(2)
        self.login_proxy.login(username='15010882898',password='123456',code='8888')
        time.sleep(5)
        #断言
        try:
            self.assertIn('我的账户',self.driver.title)
        except Exception as e:
            self.driver.get_screenshot_as_file('../shot/{}.png'.format(time.strftime('%y%m%d%H%M%S')))
            raise e
        #登陆成功后，退出账号
        self.driver.find_element_by_xpath('//*[@title="退出"]').click()

    @parameterized.expand(get_data('login_failed_data.json'))#登陆失败用例
    def test02_login_failed(self,username,password,code,expect):   #登录失败用例
        # logging.info('测试数据为：',username,password,code)
        self.index_proxy.click_login_button()
        time.sleep(2)
        self.login_proxy.login(username=username, password=password, code=code)
        # logging.info('预期结果为：',expect,'实际结果为：',get_tips_info())
        # 断言
        try:
            self.assertIn(expect, get_tips_info())
        except Exception as e:
            self.driver.get_screenshot_as_file('../shot/{}.png'.format(time.strftime('%y%m%d%H%M%S')))
            raise e