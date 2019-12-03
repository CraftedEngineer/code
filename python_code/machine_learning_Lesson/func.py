# 自定义函数
def func():  #def:关键字  func是函数的名称(看心情，想些啥，基本都可以写，除了关键字)
    #函数名称潜规则： 单词全部采用小写字母书写，如果有多个，使用下划线分割
    #()中是参数
    pass   #占位符
def my_print():
    print("a")
    print(__name__)

#函数的调用
#my_print()
if __name__ == "__main__":  #程序的入口
    my_print()