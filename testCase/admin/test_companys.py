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

    # @unittest.skip(u'跳过测试！')
    def test_queryCompanyList(self):
        # 查询定制客户列表
        self.nob = xls.get_xls('test_quercompanylist.xlsx','test_quercompanylist')


        http.set_url(self.nob[1][0])
        http.set_params({
            'userId': self.id_,
            'token': self.token,
            'companyId': 1,
            'country': 1,
            'pageNo': self.nob[1][1],#页数
            'pageSize': self.nob[1][2],
            'companyName': ''
        })
        p = http.get().json()
        print(p['msg'])
        self.assertNotEqual(self.nob[1][3], p['code'])

    # @unittest.skip(u'跳过测试！')
    def test_saveCompany(self):
        # 新建修改定制客户
        self.nob = xls.get_xls('test_servecompanys.xlsx','test_servecompanys')
        for datas in self.nob[1:]:
            http.set_url(datas[0])
            http.set_data({
                'lang':self.lang,
                'userId':self.id_,
                'token':self.token,
                'companyId':1,
                'country':1,
                'companyName':datas[1],
                'contactName':datas[2],
                'contactPhone':datas[3],
                'contactEmail':datas[4],
                'contactAddr':datas[5],
                'description':datas[6],
                'editCompanyId':datas[7]
            })
            ts = http.post().json()
            print(datas[1],ts['msg'])
            self.assertNotEqual(datas[8], ts['code'])
    @unittest.skip(u'跳过测试！')
    def test_deletCompany(self):
        #删除定制客户数据
        self.nob = xls.get_xls('test_deletcompany.xlsx','test_deletcompany')
        http.set_url(self.nob[1][0])
        http.set_params(
            {'lang':self.lang,
            'token':self.token,
            'userId':self.id_,
            'editCompanyId':self.nob[1][1]
            })
        ts = http.get().json()
        print(ts)
        self.assertNotEqual(self.nob[1][2], ts['code'])
    @unittest.skip(u'跳过测试！')
    def test_quercompanys(self):
        #根据客户名称，查询定制客户数据
        http.set_url('/company/queryCompanys')
        ts = http.get().json()
        print(ts)


