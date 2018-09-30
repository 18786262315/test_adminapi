
from common.Log import Logger
from common.configHttp import ConfigHttp
from common.commons import Readkey
import readConfig

red = readConfig.ReadConfig()
http = ConfigHttp()
log = Logger()
logger = log.get_logger()
keys = Readkey()


try:
    value = keys.get_xls('login.xlsx','user')
    user_phone = int(value[0][0])
    user_password = int(value[0][1])
    http.set_data(data={'lang':'zh-CN',
    'userId':'',
    'token':'',
    'companyId':'',
    'country':'',
    'phone':user_phone,'password':user_password})
    http.set_url('/sysUser/login')
    ts = http.post().json()
    for key,vl in ts['datas'].items():
        # 写入到配置文件
        red.set_user(str(key),str(vl))
except Exception as e:
    logger.error('this is get_token %s'%e)



