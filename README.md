# MD5LengthExtentionAttack
MD5算法的实现，对MD5进行长度拓展攻击  
思路：利用Hashpumpy工具，获取secret的MD5值，用该值再添加任意数据data进行第二次MD5，得到K1，  
      根据secret和任意数据data可以重构得到一个新的输入data’，注意此时主要是对data’的长度部分进行修改，对data’进行MD5，得到K2，    
      最后比较K1和K2的值，如果符合预期，则长度拓展攻击成功  
