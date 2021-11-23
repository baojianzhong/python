# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 05:12
# @Author : Baobao
# @File :  026_爬蟲_流程控制語句_if案例練習
# @Project : python基礎

# 在控制台上輸入一個年齡 如果您的年齡大於18了 那麼打印可以去網吧了
# input 返回值類型為字符串
age = input('請輸入您的年齡')

# 字符串和整數int是不可以比較大小的
if int(age) > 18:
    print('您成年了，可以去16網吧了')