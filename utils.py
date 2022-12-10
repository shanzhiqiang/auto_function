from selenium import webdriver

#创建工具类
class DriverUtil:
    #driver置空
    __driver = None
    #初始化驱动对象，并返回
    @classmethod
    def get_driver(cls):
        #判断驱动对象是否存在，不存在则创建
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(20)
        return cls.__driver

    #销毁驱动对象
    @classmethod
    def quit_driver(cls):
        #判断驱动对象是否存在，存在则销毁
        if cls.__driver is not None:
            cls.__driver.close()
            cls.__driver = None