
# _*_ coding : utf-8 _*_
# @Time : 2021/11/3 上午 08:39
# @Author : Baobao
# @File :  048_爬蟲_文件_文件的讀寫
# @Project : python基礎


# 寫數據
# write 寫法
#
# fp = open('demo/text.txt','a')
#
# fp.write('hello, i am here \n')
#
# fp.close()

# 讀數據

fp1 = open('demo/text.txt','r')
# 默認情況下 read時一字節一字節讀的，比較慢
# content = fp1.read()
# print(content)

# readline 是一行一行的讀取，但是只能讀取一行

# content = fp1.readline()
# print(content)

# readlines 可以按照行來讀取 但是會將所有的數據，會以列表的形式返回

content= fp1.readlines()
print(content)