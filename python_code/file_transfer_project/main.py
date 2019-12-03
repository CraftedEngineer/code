#读取明文内容
f = open("D:\重要的文件夹？！\学习\大三第一学期\密码学实验\\test.txt")
Plain_Text = f.read()
print("明文为：" + Plain_Text)
f.close()

#对明文进行哈希散列得到文件摘要
import hashlib
m = hashlib.md5()
b = Plain_Text.encode(encoding = 'utf-8')
m.update(b)
Plain_Text_md5 = m.hexdigest()
print('MD5加密前为：' + str(Plain_Text))
print('MD5加密后的摘要为:' + str(Plain_Text_md5))

#用私钥对摘要进行非对称加密
from gcd import *
from exponentiation import *
from rsa import *

#if __name__ == "__main__":
'''公钥私钥中用到的两个大质数p,q，都是1024位'''
p = 106697219132480173106064317148705638676529121742557567770857687729397446898790451577487723991083173010242416863238099716044775658681981821407922722052778958942891831033512463262741053961681512908218003840408526915629689432111480588966800949428079015682624591636010678691927285321708935076221951173426894836169
q = 144819424465842307806353672547344125290716753535239658417883828941232509622838692761917211806963011168822281666033695157426515864265527046213326145174398018859056439431422867957079149967592078894410082695714160599647180947207504108618794637872261572262805565517756922288320779308895819726074229154002310375209
'''生成公钥私钥'''
pubkey, selfkey = gen_key(p, q)
'''需要被加密的信息转化成数字，长度小于秘钥n的长度，如果信息长度大于n的长度，那么分段进行加密，分段解密即可。'''
m = int(Plain_Text_md5,16)
'''信息加密，m被加密的信息，c是加密后的信息'''
digital_signature = encrypt(m, pubkey)
print("加密后的数字签名为："+ str(digital_signature))


#将加密后的数字签名和文件进行连接
link_file = Plain_Text + str(digital_signature)

#使用AES算法对其进行对称加密
import base64
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#加密方法
def encrypt_oracle(key,text):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text
#解密方法
def decrypt_oralce(key,text):
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    #执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','')
    return decrypted_text

encrypt_file = encrypt_oracle("jianghao",link_file)
# print(encrypt_file)

#将密文输出到文件，用于传输给接收方
f = open("D:\重要的文件夹？！\学习\大三第一学期\密码学实验\\test1.txt", 'w')
f.write(encrypt_file)
f.close()


#接收方读取文件中的密文信息，用于解密
f = open("D:\重要的文件夹？！\学习\大三第一学期\密码学实验\\test1.txt")
encrypt_file = f.read()
f.close()

#接收者收到文件，利用会话密钥对加密文件进行对称算法解密
decrypt_file = decrypt_oralce("jianghao",encrypt_file)
#print(decrypt_file)

#取出明文
Plain_Text_get = decrypt_file[0:47]
print("收到的明文为：" + Plain_Text_get)
#取出数字签名
digital_signature_get = decrypt_file[47:]
#print(digital_signature_get)

#对数字签名进行公钥解密，确保文件未被修改过
digest_get = decrypt(int(digital_signature_get), selfkey)
print("收到的摘要：" + str(hex(digest_get)))
if digest_get == int(Plain_Text_md5 ,16):
    print("文件未被修改")
else:
    print("文件已被修改")


