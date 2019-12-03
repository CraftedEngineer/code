'''
安装 pip install aiml
'''
import aiml
k = aiml.Kernel()
k.learn("std-startup.xml")   #语料库
k.respond("load aiml b")

while True:
    print(k.respond(input("input >>")))
