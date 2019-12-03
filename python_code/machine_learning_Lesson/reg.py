'''
正则表达式是用来操作字符串的一种逻辑公式
'''

import re


s = "贪心学院的官网是http://www.greedyai.com"
reg = "http://[w]{3}\.[a-z0-9]*.\.com"
# result = re.findall(reg,s)
# print(result)

s = "hello greedyai hello"
reg = "hello"
print(re.findall(reg,s))  #返回值是一个数组，可以返回多个
print(re.findall(reg,s)[0])

#元字符
'''
. 代表的是换行符以外的任意字符  \n
\w 匹配字母或数字或下划线或汉字
\s 匹配任意空白符
\d 匹配任意数字 0-9
^  匹配字符串的开始
$  匹配字符串的结束
'''

s = "fasdflk浩哥s啦_~啦啦 d_df666@#"
print(re.findall("\w",s))
print(re.findall("\d",s))
print(re.findall("\s",s))
print(re.findall("^\d",s)) #开头必须是0-9的数字

#反义代码
'''
\W“：不是\w匹配的那些
\S：不是\s匹配的那些
\D：不是\d匹配的那些
'''
print(re.findall("\W",s))

# 限定符
'''
s = "贪心学院的官网是http://www.greedyai.com"
reg = "http://[w]{3}\.[a-z0-9]*.\.com"
* 它代表的是它前面的正则表达式重复0次或多次
+ 重复1次或者多次
? 重复0次或1次
{n} 重复n次
{n,} 重复n次或多次(最小重复n次)
{n,m} 重复n到m次

'''

s = "hh123hhsd123423....答复sdfff532"
print(re.findall("\d{3}",s))
print(re.findall("[\da-z]+",s))

s1 = "我的qq是42197393"
reg = "\d{5,12}"
print(re.findall(reg,s1))

#分组匹配
s = "我的qq号码是:2909548259,我的邮编是：050000"
reg = "(\d{5,12}).*(\d{5})"
reg1 = "(\d{3})(\d{2})"
#下面这一行的分组匹配就认为组1和组2是连续的内容，中间没有任何的字符
print(re.findall(reg,s))
print(re.search(reg,s).group(0)) #匹配正则表达式的所有内容
print(re.search(reg,s).group(1))
print(re.search(reg,s).group(2))
print(re.search(reg1,s).group(0))
print(re.search(reg1,s).group(1))
print(re.search(reg1,s).group(2))

#语言也是一种工具，语言也是一种应用软件
