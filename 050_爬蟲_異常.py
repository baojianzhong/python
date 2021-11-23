# _*_ coding : utf-8 _*_
# @Time : 2021/11/3 上午 09:14
# @Author : Baobao
# @File :  050_爬蟲_異常
# @Project : python基礎

try:
   fp = open('text.txt','r')
   fp.read()
   fp.close()
except FileNotFoundError:
    print('系統正在升級')