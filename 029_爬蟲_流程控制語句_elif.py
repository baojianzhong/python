# _*_ coding : utf-8 _*_
# @Time : 2021/11/2 下午 05:25
# @Author : Baobao
# @File :  029_爬蟲_流程控制語句_elif
# @Project : python基礎

grade = int(input('請輸入您的成績'))

if grade> 90:
    print('優秀')
elif grade >80:
    print('良好')
elif grade >70:
    print('中等')
elif grade > 60:
    print('及格')
else:
    print('不及格')


