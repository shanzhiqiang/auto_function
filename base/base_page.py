from utils import DriverUtil


#创建对象库层基类
class BasePage:
    #初始化驱动对象
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    #定义元素定位信息方法，并返回元素
    def base_find_element(self,location):
        return self.driver.find_element(location[0],location[1])

#创建操作层基类
class BaseHandle:
    #定义元素输入操作
    def base_input_text(self,element,text):
        element.clear()
        element.send_keys(text)