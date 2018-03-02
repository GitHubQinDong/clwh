'''1 bin(x) 1.1. 将一个整形数字转换成二进制字符串'''
# print(bin(3))
# print(bin(-10))
# print(type(bin(3))) #获取b的类型
'''输出结果如下：
0b11
-0b1010
class 'str'>
'''
'''1.2. 如果参数x不是一个整数，则x必须定义一个 __index__() 方法，并且方法返回值必须是整数。
1.2.1 如果对象不是整数，则报错'''
# class A:
#     pass
# a = A()
# print(bin(a))
'''Traceback (most recent call last):
  File "E:/untitledPyQt/LL/LL5.py", line 91, in <module>
    print(bin(a) )
TypeError: 'A' object cannot be interpreted as an integer'''
'''1.2.2 如果对象定义了__index__方法，但返回值不是整数，报错'''
# class B:
#     def __index__(self):
#         return "3"
# b = B()
# print(bin(b))
'''Traceback (most recent call last):
  File "E:/untitledPyQt/LL/LL5.py", line 101, in <module>
    print(bin(b))
TypeError: __index__ returned non-int (type str)'''
'''1.2.3 对象定义了__index__方法，且返回值是整数，将__index__方法返回值转换成二进制字符串'''
# class C:
#     def __index__(self):
#         return 0xa
# c = C()
# print(bin(c))
'''输出结果如下：0b11'''


'''2 oct() 函数将一个整数转换成8进制字符串。'''
'''oct 语法：oct(x)'''
'''参数说明：
    x -- 整数。'''
'''返回8进制字符串。'''
'''实例
以下实例展示了 oct 的使用方法：'''
# print(oct(10))
# '''0o12'''
# print(oct(20))
# '''0o24'''
# print(oct(15))
# '''0o17'''


'''3 int()函数用于将一个字符串或数字转换为整型。
以下是int()方法的语法:
class int(x, base=10)
参数
      x - - 字符串或数字。
      base - - 进制数，默认十进制。
返回整型数据。
以下展示了使用int()方法的实例：'''
'''不传入参数时，得到结果0'''
# print(int())
# '''0'''
# print(int(3))
# '''3'''
# print(int(3.6))
# '''3'''
'''如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制'''
# print(int('12', 16))
# '''18'''
# print(int('0xa', 16))
# '''10'''
# print(int('10', 8))
# '''8'''
'''1.x可以是数字或字符串，但是base被赋值后x只能是字符串
2.x作为字符串时必须是base类型，也就是说x变成数字时必须能用base进制表示'''
'''实例：
1.x是数字的情况：'''
# print(int(3.14))
# '''3'''
# print(int(2e2))
# '''200'''
# print(int(100, 2))
# '''出错，base 被赋值后函数只接收字符串'''
'''2.x是字符串的情况：'''
# print(int('23', 16))
# '''35'''
# print(int('Pythontab', 8))
# '''出错，Pythontab不是个8进制数'''
'''3.base可取值范围是2~36，囊括了所有的英文字母(不区分大小写)，十六进制中F表示15，那么G将在二十进制中表示16，依此类推....Z在三十六进制中表示35'''
# print(int('FZ', 16))
# '''出错，FZ不能用十六进制表示'''
# print(int('Fy', 35))
# '''575'''
# '''4.字符串0x可以出现在十六进制中，视作十六进制的符号，同理0b可以出现在二进制中，除此之外视作数字0和字母x'''
# print(int('10',16))
# '''16，0x是十六进制的符号'''
# print(int('0x10', 17))
# '''出错，'0x10'中的 x 被视作英文字母 x'''
# print(int('0x10', 36))
# '''42804，36进制包含字母 x'''



'''4 hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。'''
'''hex 语法：hex(x)'''
'''参数说明：
    x -- 10进制整数'''
'''返回16进制数，以字符串形式表示。
实例
以下实例展示了 hex 的使用方法：'''
# print(hex(255))
# '''0xff'''
# print(hex(-42))
# '''-0x2a'''
# print(hex(19))
# '''0x13'''
# print(hex(12))
# '''0xc'''
# print(type(hex(12)))
# '''<class 'str'>      # 字符串'''


'''5 float()函数用于将整数和字符串转换成浮点数。
float()方法语法：class float([x])
参数
    x - - 整数或字符串
返回浮点数。
以下实例展示了
float()的使用方法：'''
# print(float(0x10))
# '''1.0'''
# print(float(112))
# '''112.0'''
# print(float(-123.6))
# '''-123.6'''
# print(float('123')) # 字符串
# '''123.0'''



'''6 complex()函数用于创建一个值为real + imag * j
的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。
complex
语法：class complex([real[, imag]])
参数说明：
real - - int, long, float或字符串；
imag - - int, long, float；
返回一个复数。
实例
以下实例展示了complex的使用方法：'''
# print(complex(1, 2))
# '''(1 + 2j)'''
# print(complex(1))  # 数字
# '''(1 + 0j)'''
# print(complex("1"))  # 当做字符串处理
# '''(1 + 0j)'''
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
# print(complex(1.3,3))
# '''(1 + 2j)'''



'''7 class bool([x])
返回一个布尔值，即True或False。x是使用标准的真理测试程序转换的。
如果x为false或省略，则返回false;否则返回True。bool类是int的子类
(请参阅数值类型int、float和complex)。
它不能被进一步细分。它的惟一实例是False和True(请参阅布尔值)。'''
'''整数0，浮点数0.0，空列表，空元组，空字典，空字符串，均为False'''
# print (bool(6.40),bool(0),bool([]),bool(()),bool({}),bool(' '))
'''正数，负数均为True'''
# print(bool(8),bool(-3),bool(-3.9),bool(9.8))
'''非空列表，非空元组，非空字典，非空字符串均为True'''
# print(bool([2,3]),bool((3,4)),bool({'name':'song'}),bool('python'))
'''结果：
False False False False False False
True True True True
True True True True'''
'''另外，注意：bool是int的子类：'''
# print(issubclass(bool,int))
'''True'''
'''bool类只有True和False两个实例：'''
# print(isinstance(True,bool))
'''True'''
# print(isinstance(False,bool))
'''True'''


'''8 abs(x) 返回一个数字的绝对值。参数可以是整数或浮点数。如果参数是复数，则返回其大小'''
# x=abs(-1.23)
# print(x)
# x=abs(3+4j)
# print(x)
'''输出结果如下：1.23'''



'''9 round() 方法返回浮点数x的四舍五入值。
以下是 round() 方法的语法:round( x [, n]  )
参数
    x -- 数值表达式。
    n -- 数值表达式。
返回浮点数x的四舍五入值。
以下展示了使用 round() 方法的实例：
#!/usr/bin/python'''
# print(round(80.23456, 1))
# print(round(100.000056, 5))
# print(round(-100.000056, 2))

'''以上实例运行后输出结果为：

round(80.23456, 2) :  80.23
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0'''

'''python中关于round函数的小坑
这个一直都想写，但是因为这个点比较小，所以一直懒得动手。不过还是补上吧，留着早晚是个祸害。
round函数很简单，对浮点数进行近似取值，保留几位小数。比如'''
# print(round(10.0 / 3, 2))
# '''3.33'''
# print(round(20 / 7))
# '''3'''
'''第一个参数是一个浮点数，第二个参数是保留的小数位数，可选，如果不写的话默认保留到整数。
这么简单的函数，能有什么坑呢？
1、round的结果跟python版本有关我们来看看python2和python3中有什么不同：
复制代码
$ pythonPython2.7.8'''
# print(round(0.5))
'''1.0'''
# print(round(0.5))
'''0'''
'''复制代码好玩吗？
如果我们阅读一下python的文档，里面是这么写的：在python2.7的doc中，round()的最后写着，
 保留值将保留到离上一位更近的一端（四舍六入），如果距离两端一样远，则保留到离0远的一边。所以round(0.5)
会近似到1，而round(-0.5)会近似到 - 1。但是到了python3.5的doc中，文档变成了
如果距离两边一样远，会保留到偶数的一边。比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。
所以如果有项目是从py2迁移到py3的，可要注意一下round的地方（当然，还要注意 / 和 //，还有print，
还有一些比较另类的库）。
2、特殊数字round出来的结果可能未必是想要的。'''
# print(round(2.675, 2))
'''2.67'''
'''python2和python3的doc中都举了个相同的栗子，原文是这么说的：
 简单的说就是，round(2.675, 2)的结果，不论我们从python2还是3来看，结果都应该是2.68的，结果它偏偏是2.67，为什么？
 这跟浮点数的精度有关。我们知道在机器中浮点数不一定能精确表达，因为换算成一串1和0后可能是无限位数的，
 机器已经做出了截断处理。那么在机器中保存的2.675
这个数字就比实际数字要小那么一点点。这一点点就导致了它离2.67要更近一点点，所以保留两位小数时就近似到了2.67。
以上。除非对精确度没什么要求，否则尽量避开用round()函数。近似计算我们还有其他的选择：
使用math模块中的一些函数，比如math.ceiling（天花板除法）。python自带整除，python2中是 /，3中是 //，
还有div函数。字符串格式化可以做截断使用，例如
"%.2f" % value（保留两位小数并变成字符串……如果还想用浮点数请披上float()
的外衣）。当然，对浮点数精度要求如果很高的话，请用嘚瑟馍，不对不对，请用decimal模块。就酱。'''



'''10 pow()
方法返回xy（x的y次方） 的值。
以下是math模块pow()方法的语法:'''
'''import math
math.pow(x,y)
内置的pow()方法pow(x, y[, z])
函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x, y) % z
注意：pow()通过内置的方法直接调用，内置方法会把参数作为整型，而math模块则会把参数转换为float。参数
x - - 数值表达式。
y - - 数值表达式。
z - - 数值表达式。
返回值返回xy（x的y次方） 的值。
以下展示了使用pow()方法的实例：
# !/usr/bin/python
# -*- coding: UTF-8 -*-'''
# import math  # 导入 math 模块
# print(math.pow(100, 2))
# # 使用内置，查看输出结果区别
# print(pow(100, 2))
# print(math.pow(100, -2))
# print(math.pow(2, 4))
# print(math.pow(3, 0))
'''以上实例运行后输出结果为：
math.pow(100, 2): 10000.0
pow(100, 2): 10000
math.pow(100, -2): 0.0001
math.pow(2, 4): 16.0
math.pow(3, 0): 1.0'''

'''11 python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
在 python 2.3 版本之前不允许处理复数。
函数语法divmod(a, b)
参数说明：
    a: 数字
    b: 数字
实例'''
# print(divmod(7, 2))
# '''(3, 1)'''
# print(divmod(8, 2))
'''(4, 0)'''
'''中文说明：divmod(a,b)方法返回的是a//b（商）以及a%b(余数)，返回结果类型为tuple
[python] view plain copy'''
# print(divmod(9,2))
# '''(4, 1)'''
# print(divmod(9,2)[0])
# '''4'''
# print(divmod(9,2)[1] )
# '''1'''

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
# print(all(['a', (2, 4), 1, True]))
# '''list都为"真"'''
# '''True'''
# print(all(['a', (), 1, True]))
# '''list元素中有空tuple'''
# '''False'''
# print(all(['a', (2, 4), 0, True]))
# '''False'''
# print(all(['a', (2, 4), 3, False]))
# '''False'''
# print(all([]))
# '''True'''
# print(all(()))
# '''True'''
# print(all({}))
# '''True'''
# print(all(''))
'''True'''
'''3 any(iterable)iterable的任何元素都为False、0，''，或者iterable全为空，
则any(iterable)为False，也就是说所有的iterable都为'假'，
则any(iterable)为False，"全‘假’为False，有‘真’为True"
如果iterable的任何元素为真，返回True。如果iterable是空的，
返回False。相当于'''
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
'''这两个函数的参数都是iterable，也就是为list或者tuple'''
# print(any(['a',(2,4),3,True]))
# '''True'''
# print(any(['a',(2,4),3,False]))
# '''True'''
# print(any(['a',(),3,False]))
# '''True'''
# print(any(['',(),0,False]))
# '''False'''
# print(any(('a',(),3,False)))
# '''True'''
# print(any(('',(),0,False)))
# '''False'''
# print(any(()))
# '''False'''
# print(any([]))
# '''False'''
# print(any(''))
# '''False'''
# print(any({}))
'''False'''
'''all()："有‘假’为False，全‘真’为True，iterable为空是True"
any()："有‘真’为True，全‘假’为False，iterable为空是False"'''


#4 ascii(object) 这个函数跟repr()函数一样，返回一个可打印的对象字符串方式表示。当遇到非ASCII码时，
# 就会输出\x，\u或\U等字符来表示。与Python 2版本里的repr()是等效的函数。

'''例子：'''
# print(ascii(10), ascii(9000000), ascii('b\31'), ascii('0x\1000'))

'''输出结果如下：
10   9000000   'b\x19'   '0x@0' '''




'''7 class bytearray([source[, encoding[, errors]]])
返回一个新的字节数组。bytearray类是范围0 <= x < 256的整数的可变序列。
它拥有大多数常用的可变序列方法，在可变序列类型中描述，以及字节类型所拥有的大多数方法，如字节和Bytearray操作。
可选的源参数可用于以几种不同的方式初始化数组:如果它是一个字符串，您还必须给出编码
(以及可选的错误)参数;bytearray()然后使用str.encode()将字符串转换为字节。如果它是一个整数，
那么数组将具有这个大小，并且将以null字节初始化。如果它是符合缓冲区接口的对象，则将使用对象的只读
缓冲区来初始化字节数组。如果它是可迭代的，那么它必须是在0 <= x < 256的范围内的整数的iterable，
它被用作数组的初始内容。如果没有参数，将创建一个大小为0的数组。还可以看到二进制序列
类型字节、bytearray、memoryview和bytearray对象。'''

'''8 class bytes([source[, encoding[, errors]]])
返回一个新的字节对象，它是在0 <= x < 256的范围内的一个不可变的整数序列。字节是bytearray的不可变版本，
它具有相同的非突变方法和相同的索引和切片行为。因此，构造函数参数被解释为bytearray()。字节对象也可以用文字创建，
请参阅字符串和字节文字。还可以看到二进制序列类型字节、bytearray、memoryview、bytes对象、字节和bytearray操作。'''
'''
bytes是byte的序列，而str是unicode的序列。
str 使用encode方法转化为 bytes
bytes通过decode转化为str
str转换成bytes：
'''
'''9 callable(object)
1. 方法用来检测对象是否可被调用，可被调用指的是对象能否使用()括号的方法调用。'''
# print(callable(callable))
'''True'''
# print(callable(1))
'''False'''
# print(1())
'''Traceback (most recent call last):
  File "E:/untitledPyQt/LL/LL5.py", line 163, in <module>
    print(1())
TypeError: 'int' object is not callable
'''
'''2. 可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功。'''
'''3. 类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法。
'''
# class A: #定义类A
    # pass
# print(callable(A)) #类A是可调用对象
'''True'''
# a = A() #调用类A
# print(callable(a))#实例a不可调用
'''False'''
# print(a()) #调用实例a失败
'''Traceback (most recent call last):
  File "E:/untitledPyQt/LL/LL5.py", line 179, in <module>
    print(a()) #调用实例a失败
TypeError: 'A' object is not callable
'''


# class B: #定义类B
#     def __call__(self):
#         print('instances are callable now.')
# print(callable(B)) #类B是可调用对象
'''True'''
# b = B() #调用类B
# print(callable(b)) #实例b是可调用对象
'''True'''
# print(b()) #调用实例b成功
'''instances are callable now.
None
如果对象参数看起来是可调用的，则返回True，否则为False。如果返回true，则仍然有可能调用失败，
但如果是false，调用对象将永远不会成功。注意，类是可调用的(调用类返回一个新实例);
如果类具有__call__()方法，则实例是可调用的。新版本3.2:该函数首先在Python 3.0中删除，然后在Python 3.2中恢复。'''

'''10 chr(i)
返回表示一个字符的字符串，该字符的Unicode代码点是整数i。例如，chr(97)返回字符串'a'，
而chr(8364)返回字符串' '。这是ord()的倒数。参数的有效范围从0到1,114111(在基数16中为0x10FFFF)。
如果我不在这个范围内，就会产生ValueError。'''
'''参数是0 - 256 的一个整数，返回值是当前整数对应的ascii字符。参数可以是10进制也可以是16进制的形式


十六进制：'''
print (chr(0x30), chr(0x31), chr(0x61))
'''0 1 a'''


'''十进制：'''
print (chr(48), chr(49), chr(97))
'''0 1 a  '''

