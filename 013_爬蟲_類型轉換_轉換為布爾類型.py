# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 03:27
# @Author : Baobao
# @File :  013_爬蟲_類型轉換_轉換為布爾類型
# @Project : python基礎


# 如果對非0的整數進行bool類型轉換的時候，都將轉換為True
a=1
print(type(a))

b=bool(a)
print(b)
print(type(b))

# 字符串
# 只要字符串中由內容，那麼在強制類型轉換為bool時， 都為true

c='tt'
e=bool(c)
print(type(e))

# 列表
# 如果列表中什麼數據都沒有時 返回為False
f=['1','2','3']
print(type(f))
f1=bool(f)
print(f1)
print(type(f1))

g=[]
print(type(g))
g1=bool(g)
print(g1)
print(type(g1))

# 元組
# 如果元組中沒有數據的話 就返回False
h=()
print(h)
h1=bool(h)
print(h1)
print(type(h1))

# 字典
# 只要字典中有內容 那麼在強制類型為bool時返回False
j = {}

print(j)
j1=bool(j)
print(j1)
print(type(j1))


# 什麼情況下是False
# 1. 值為0
# 2. 值為0.0
# 3. 值為空的字符串，空的元組，空的字典。空的列表

