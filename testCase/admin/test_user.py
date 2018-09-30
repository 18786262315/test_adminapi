import HTMLTestRunner
import unittest
from common.Log import Logger
from common.configHttp import ConfigHttp
from common.commons import Readkey
import readConfig

red = readConfig.ReadConfig()
http = ConfigHttp()
log = Logger()
logger = log.get_logger()
xls = Readkey()


class MyTest(unittest.TestCase):  #继承unittest.TestCase
    @classmethod
    def setUpClass(self):
        print("----->>>>test_companys")
        #读取数据
        self.id_ = red.get_user('id')
        self.token = red.get_user('token')
        self.lang = red.get_http('lang')
    @classmethod
    def tearDownClass(cls):
        print("--->>>end")


