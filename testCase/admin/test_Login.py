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
keys = Readkey()

class MyTest(unittest.TestCase):#继承unittest.TestCase
     
    @classmethod
    def setUpClass(cls):
        '''登录并获取用户返回参数'''
        print ("----->>>>test_login")
        

    @classmethod
    def tearDownClass(cls):
        print ("--->>>end")

    # def tearDown(self):
    #     #每个测试用例执行之后做操作
    #     print('111')
    # def setUp(self):
    #     #每个测试用例执行之前做操作
    #     print(22222)
    # @unittest.skip(u'跳过账号登录测试！')
    def test_login(self):
        # 测试登录接口
        value = keys.get_xls('login.xlsx','user')
        for datas in value:
            http.set_data(data={'phone':str(datas[0]),'password':str(datas[1])})
            http.set_url('/sysUser/login')
            ts = http.post().json()
            print(datas[0],datas[1],ts['msg'])
            self.assertEqual(str(datas[2]),ts['code'])


