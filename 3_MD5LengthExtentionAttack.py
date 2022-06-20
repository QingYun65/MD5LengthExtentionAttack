#import hashpumpy
from hashlib import md5


key_1=b'flag{1234567890abcdef123456}Hello_World'
print("key的MD5摘要：",md5(key_1).hexdigest())

#key中"flag{1234567890abcdef123456}"为内容未知但长度(28)已知，另外 'This_is_salt'为已知
key=b'flag{1234567890abcdef123456}This_is_salt'
print("key的MD5摘要：",md5(key).hexdigest())

#计算长度拓展攻击参数，包括任意数据即重构以后新数据的长度
#其中直接运行程序，result的结果不会正确显示，并且报DeprecationWarning: PY_SSIZE_T_CLEAN will be required for '#' formats
#可以单独执行result = hashpumpy.hashpump('112bba932266ca5df55eb36dcd7050ec','This_is_salt','xx',28)，再print(result)，可以获得结果
#('0583c1213d01febfd7ecc0f6ab5ae450', b'This_is_salt\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x01\x00\x00\x00\x00\x00\x00xx')
#明确b'This_is_salt\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x01\x00\x00\x00\x00\x00\x00xx'，我们需要得到的就是对secret的填充部分
result = hashpumpy.hashpump('112bba932266ca5df55eb36dcd7050ec','This_is_salt','xx',28)
print("(MD5_value,length_append):",result)

#验证长度拓展攻击的正确性
flag = b'flag{1234567890abcdef123456}'
append = b'This_is_salt\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x01\x00\x00\x00\x00\x00\x00xx'
print("verify_MD5_value:",md5(flag+append).hexdigest()) 


#另一组攻击
key_1=b'flag{1234567890abcdef123456}Hello_World'
print("key的MD5摘要：",md5(key_1).hexdigest())
result_1 = hashpumpy.hashpump('','Hello_World','QingYun',28)
#result_1=('239b90d2bf37aabe537ada6897594b80', b'Hello_World\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x01\x00\x00\x00\x00\x00\x00QingYun')
print("(MD5_value,length_append):",result_1)
append_1=b'Hello_World\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x01\x00\x00\x00\x00\x00\x00QingYun'
print("verify_MD5_value:",md5(flag+append_1).hexdigest())