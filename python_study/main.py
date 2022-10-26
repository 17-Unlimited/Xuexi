#1.结果一致 str4除外
# str1 = 'hhhhh'
# str2 = "hhhhh"
# str3 = '''hhhhh'''
# str4 = '''h
# hh
# hh'''
# print(str1)
# print(str2)
# print(str3)
# print(str4)

#2.打印结果为hh'h'hh
# str1 = "hh'h'hh"
# str2 = 'hh\'h\'hh'
# str3 = '''hh"h"hh'''
# print(str1)
# print(str2)
# print(str3)

#3.python自动实现类型转换,print 0.5
# int1 = 1/2
# print(int1)

#4.bool运算，and、or、not,注意True，False首字母大写
# bool1 = True
# bool2 = False
# print(bool1 and bool2)
# print(True and False)

#5.空值None
# print(None)

#6.变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如 Java 是静态语言
# a = 'sssssss'
# print(a)
# a = 12
# print(a)

#6.可以多个变量赋值
# a, b, c = 1, 2, "liangdianshui"

#7.列表[]
# list1=['两点水','twowter','liangdianshui',123]
# print(list1[0:4])#后一个取不到
# print(list1[:])

#8.list
# name = ['一点水', '两点水', '三点水', '四点水', '五点水']
# name[1]='2点水'# 通过索引对列表的数据项进行修改或更新
# print(name)
# name.append('六点水')# 使用 append() 方法来添加列表项
# print(name)
#
# name = ['一点水', '两点水', '三点水', '四点水', '五点水']
# print(name)
# del name[3]# 使用 del 语句来删除列表的的元素
# print(name)

# 9.list  pop and remove
# user=['liangdianshui','twowater','两点水']
# # 突然发现之前弄错了，“茵茵”就是'VIP用户'，因此，需要删除“茵茵”；pop() 删除 list 末尾的元素
# user.pop()
# print('\n6.删除末尾用户')
# print(user)
#
# # 过了一段时间，用户“liangdianshui”不玩这个产品，删除了账号
# # 因此需要要删除指定位置的元素，用pop(i)方法，其中i是索引位置
# user.pop(1)
# print('\n7.删除指定位置的list元素')
# print(user)
#
# # remove 用法
# user=['liangdianshui','twowater','两点水']
# user.remove('twowater')
# print(user)
# 3、for 循环也可以迭代 dict （字典）

# for key in dict1 :    # 迭代 dict 中的 key
#     print ( key , end = ' ' )

# dict1 = {'name':'两点水','age':'23','sex':'男'}
# print(dict1.get('name1',"hhhh"))

# 1、字符创创建迭代器对象
# str1 = 'liangdianshui'
# iter1 = iter ( str1 )
# for x in str1 :
#     print ( x , end = ' ' )

name = ('一点水', '两点水', '三点水', '四点水', '五点水')
print(name.count('一点水'))
print(name[:])

name1 = list(name)
#list tuple dict
#list:

dict={1:'a',2:'b',3:'c',4:'d'}

#获取字典的key和value列表
tuple_keys = dict.keys()
print(list(dict.values()))
iter_dict = dict.items()
print(iter_dict)
print(list(dict.items()))

#遍历字典的key和value
for k in dict.keys():
    print(k)
for v in dict.values():
    print(v)
for k,v in dict.items():
    print(k, v)

import jieba
# jieba分词返回的是迭代器，因此不能直接作为tokenize
print(jieba.cut("我爱北京天安门"))

#10. enumerate()
# 通常情况下，您枚举字典的键：
#
# example_dict = {1:'a', 2:'b', 3:'c', 4:'d'}
#
# for i, k in enumerate(example_dict):
#
# print(i, k)
#
# 输出：
#
# 0 1
#
# 1 2
#
# 2 3
#
# 3 4
#
# 但是，如果要同时枚举键和值，则可以这样：
#
# for i, (k, v) in enumerate(example_dict.items()):
#
# print(i, k, v)
#
# 输出：
#
# 0 1 a
#
# 1 2 b
#
# 2 3 c
#
# 3 4 d

# 11.# 在行上更改
# import torch
# a = torch.tensor([1, 2, 3])   # C：一行三列
# c = a.expand(2, 3) # 将C进行扩为：两行三列
# print(a)
# print(c)
# # 输出信息：
# tensor([1, 2, 3])
# tensor([[1, 2, 3],
#         [1, 2, 3]]

# 12.矩阵相乘
# 1. torch.mm
# 该函数即为矩阵的乘法，torch.mm(tensor1, tenor2)，参与计算的两个张量必须为二维张量（即矩阵），其结果张量out的维度关系满足：
# o u t ( p × q ) = t 1 ( p × m ) ∗ t 2 ( m × q )

# 2. torch.bmm
# 该函数提供了batch维度的矩阵乘法运算，即batch内对应的矩阵两两相乘，因此要求参与计算的两个张量必须为三维张量，其中第一个维度为batch_size，必须相同，其结果张量 out的维度关系满足：
# o u t ( b × p × q ) = t 1 ( b × p × m ) ∗ t 2 ( b × m × q )

# 3. torch.matmul
# 该函数的功能相较于前面两个要丰富的多，其支持参与运算的两个张量有不同的维度，计算的机理也各不相同，具体包括：
#
# (1) 两个张量均为1维张量（即向量）时，计算向量的内积
#
# (2) 两个张量均为2维张量（即矩阵）时，计算矩阵的乘法
#
# (3) 第一个向量为1维张量，第二个张量为2维张量，对第一个张量视情进行broadcast，然后进行矩阵乘法，在将上述结果squeeze为1维；
#
# (4) 第二个向量为1维张量，第一个张量为2维张量，计算矩阵和向量的乘法；
#
# (5) 两个向量维度至少为1，且其中至少一个张量的维度大于2；则先进行broadcast，然后进行bmm操作，最后将上述结果转换会broadcast之前的效果。



