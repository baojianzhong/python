# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 02:39
# @Author : Baobao
# @File :  010_爬蟲_數據類型_列表_元組_字典
# @Project : python基礎

# list 列表
# tuple 元組
# dict 字典

# list 列表
# 應用場景 ： 當獲取到了很多個數據的時候，那麼我們可以將他們存儲到列表中 然後直接使用列表訪問
name_list = ['周杰倫','科比']
print(name_list)


# tuple 元組

age_tuple =(18,19,20,21)
print(age_tuple)

# dict 字典
# 應用場景： scrapy 框架使用
person = { 'name':'紅浪漫','age': 18}
print(person)

print(type(person))

a = 1.5
print(type(a))
