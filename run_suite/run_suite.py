import unittest
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('../script/')

with open('../report/report.html','wb') as f:
    runner = HTMLTestRunner(stream=f,title='TPshop测试报告')
    runner.run(suite)