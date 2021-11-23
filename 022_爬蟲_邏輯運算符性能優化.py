# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 04:45
# @Author : Baobao
# @File :  022_爬蟲_邏輯運算符性能優化
# @Project : python基礎


a=36
# and 的性能優化 黨and前面的結果為false 的情況下 ，就不再執行後面的代碼了
a < 10 and print('hello word')

# or 的性能優化
5 > 5 or print('Hello word')