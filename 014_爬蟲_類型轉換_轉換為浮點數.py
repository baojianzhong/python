# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 03:16
# @Author : Baobao
# @File :  014_爬蟲_類型轉換_轉換為浮點數
# @Project : python基礎

# 黨我們在爬蟲的時候大部分獲取的都是字符串數據類型

a='12.34'
print(type(a))

# 將字符串類型的數據轉化為浮點數據
b=float(a)
print(b)
print(type(b))

c=666
print(c)
print(type(c))

e=float(c)
print(e)
print(type(e))

