import yagmail
import readConfig

#链接邮箱服务器

red = readConfig.ReadConfig()

host = red.get_email('mail_host') #所用邮箱开发商
username = red.get_email('mail_user')  # 账号
pas = red.get_email('mail_pass')  #密码，此处的pas是授权码

title = red.get_email('title')  #邮件名称
content = red.get_email('content')  #内容
sender = red.get_email('sender')  #单一用户发送
receiver = red.get_email('receiver')  #多用户发送

for i in list(receiver):
    print(i)
yag = yagmail.SMTP(
    user=username, 
    password=pas, 
    host=host)
# # 邮箱正文
contents = [content]

# # 发送邮件

# yag.send('843092012@qq.com', title, contents)

# # 给多个用户发送邮件

# yag.send(receiver,title, contents)

# # # 发送邮件带附件

# yag.send('843092012@qq.com', title, contents,
#          ["E:\\新联国际\\bq包\\test_img\\床01.png"])
