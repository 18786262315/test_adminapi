# --*-- coding:utf-8 --*--
import HTMLTestRunner
import unittest
from common.configHttp import ConfigHttp
from common.Log import Logger
# import json
localhttp = ConfigHttp()

log = Logger()
logger = log.get_logger()


class MyTest(unittest.TestCase):  #继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        print("开始执行test_main---->")

    @classmethod
    def tearDownClass(cls):
        print("end----->")

    def tearDown(self):
        #每个测试用例执行之后做操作
        print('---')

    def setUp(self):
        #每个测试用例执行之前做操作
        print('---')

    def test_run(self):
        self.assertEqual(1, 1)

        #测试用例
    def test_run2(self):
        data = {'Content-Type': 'application/x-www-form-urlencoded'}
        localhttp.set_headers(data)

        localhttp.set_data(
            data={
                'lang': 'zh-CN',
                'userId': 16,
                'token': '7e524b6202ca4a41881c6bdcf7133109',
                'companyId': 1,
                'country': 1,
                'brandName': '',
                'pageNo': 1,
                'pageSize': 5
            })

        localhttp.set_url('/brand/queryBrandList')
        kes = localhttp.post().json()
        sds = type(kes['code'])
        self.assertIs(200, kes['msg'])

        #测试用例
    def test_run3(self):
        # self.assertEqual(1,1)
        localhttp.get()
        self.assertIs(1, 1)
        #测试用例
    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
