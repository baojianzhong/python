# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 03:07
# @Author : Baobao
# @File :  013_爬蟲_類型轉換
# @Project : python基礎

# 轉換為整型
# str --> int

a ='123'
print(type(a))

# 將字符串轉換為整數
b= int(a)
print(type(b))

# float --> int
# 如果將float轉化為整數 那麼會返回小數點前面的數據
c= 1.6
print(type(c))

d= int(c)
print(d)
print(type(d))


# boolean --> int
# 前置類型轉換為誰 就寫什麼方法

e=False
print(type(e))

f=int(e)
print(f)
print(type(f))

# 如果字符串中包含特殊字符，則無法轉換成功