import unittest, HTMLTestRunner,os
import set_token,readConfig

suite = unittest.TestSuite()  #创建测试套件
all_cases = unittest.defaultTestLoader.discover('testCase/admin', 'test_*.py')

#找到某个目录下所有的以test开头的Python文件里面的测试用例

for case in all_cases:
    suite.addTests(case)  #把所有的测试用例添加进来

fp = open( os.path.join(readConfig.proDir,'result','res.html'), 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp, verbosity=2, title='测试结果：', description='所有测试情况')
runner.run(suite)
#运行测试
