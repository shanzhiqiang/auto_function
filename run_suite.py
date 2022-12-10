import unittest
from HTMLTestReportCN import HTMLTestRunner

from tools.config import BASE_PATH

suite = unittest.defaultTestLoader.discover('script/')

with open(BASE_PATH+'/report/report.html','wb') as f:
    runner = HTMLTestRunner(stream=f,title='TPshop测试报告')
    runner.run(suite)