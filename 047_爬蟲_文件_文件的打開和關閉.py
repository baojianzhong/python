# _*_ coding : utf-8 _*_
# @Time : 2021/11/3 上午 08:20
# @Author : Baobao
# @File :  049_爬蟲_文件_文件的打開和關閉
# @Project : python基礎


# 創建一個test.txt文件
# open(文件路徑,模式)
# 模式： w 可寫
#       r 可讀

# open('test.txt','w')

# fp = open('test.txt','w')
# fp.write('hello world')


# 文件夾是不可以創建的 暫時需要手動創建

fp = open('demo/text2.txt','w' )
fp.write('hello foxconn')

# 文件的關閉

fp.close()
