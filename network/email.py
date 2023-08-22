# This code is using the yagmail library to send an email from a specified email account to a list of
# recipients. The SMTP function is used to establish a connection to the email server, and the send
# function is used to send the email with a subject, contents, and optional cc recipients. Finally,
# the close function is used to close the connection to the email server.
import yagmail

# 创建一个邮件对象
mail = yagmail.SMTP("python3721@163.com", "授权码", "smtp.163.com")
# 发送内容
contents = ["早上好，", "昨日网站的新增用户为 83.7 万人，", "请查收。"]
# 接收邮件的邮箱地址
to_list = ["同事A@163.com", "同事B@163.com", "同事C@163.com"]
# 发送邮件
mail.send(to_list, "测试邮件", contents, cc="上级D@163.com")
# 关闭邮件
mail.close()