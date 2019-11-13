# import time
# #获取时间戳
# def t_stamp():
#     t = time.time()
#     t_stamp = str(int(t))
#     print('当前时间戳:', t_stamp)
#     return t_stamp
# t_stamp()
# import re
# # f = open('license(2).html','r+',encoding='utf8')
# # message = f.read()
# f = open('1.txt','r+',encoding='utf8')
# message = f.read()
# # print(message)
# bb = r"(?<=<p).(?=..?.?</p>)"
# bc = re.compile(bb)
# # print(bc.findall(message))
# newKey = re.sub(r"(?<=<p).(?=..?.?.?</p>)", " id='order'>", message)
# f.seek(0)
# f.truncate()
# f.write(newKey)
# print(newKey)
# f.close()
a = input()
print(type(a))
