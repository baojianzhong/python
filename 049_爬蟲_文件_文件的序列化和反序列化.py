# _*_ coding : utf-8 _*_
# @Time : 2021/11/3 上午 08:50
# @Author : Baobao
# @File :  049_爬蟲_文件_文件的序列化和反序列化
# @Project : python基礎

# 序列化和反序列化

# 序列化   對象---》字節序列
# 反序列化 字節序列--》對象

# fp = open('test.txt','w')
# # fp.write('hello world!')
# 默認情況下對象是無法寫入到文件中的
# name_list = ['張三','李四']
# fp.write(name_list)
# fp.close()


# 序列化的兩種方式
# dumps()
# 1. 創建一個文件
# fp = open('test.txt','w')
# 2. 定義一個列表
# name_list =['zs','ls']
# 導入json模塊到文件中
import json

# 序列化
# 將python對象編程json字符串
# 我們在使用scrapy框架的時候 該框架會返回一個對象
# 我們要講對象寫入到文件中 就要使用json.dumps
# names = json.dumps(name_list)
# fp.write(names)
# fp.close()

# dump
# 在講對象轉換為字符串的統統是，指定一個文件的對象

# fp = open('test.txt','w')
# name_list =['zs','ls','ww']
#
# import json
# # 相當於names=json.dumps(name_list) 和 fp.write(names)
# json.dump(name_list,fp)
# fp.close()


# 反序列化
# 將json的字符串變成一個python對象

# loads
# import json
# fp = open('test.txt','r')
# content = fp.read()
# result= json.loads(content)
#
# print(result)
# print(type(result))



# load
import json
fp = open('test.txt','r')
result= json.load(fp)

print(result)
print(type(result))

fp.close()