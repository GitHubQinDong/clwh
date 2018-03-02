# def foo(arg,a):
#     x=100
#     y='hello python'
#     for i in range(10):
#         j=1
#         k=i
#     def b(a):
#         print(locals())
#     b(a)
#     print(locals())
#
# foo(1,2)
# print(locals())

# class A:
#     def __init__(self):
#         self.name='zhangsan'
#     def method(self):
#         print('method print')
# instance=A()
# print(getattr(instance,'name','not find'))
# print(getattr(instance,'age','not find'))
# print(getattr(instance,'method','default'))

# class Shape:
#     def __dir__(self):
#         return ['area','perimeter','location']
# s=Shape()
# print(dir(s))
# print(dir())
# a='abcd'
# print(len(s))

class test():
    name='xiaohua'
    def run(self):
        return 'hello world'
t=test()
t1=test()
test.name='lisi'

print(t.name+'%%%%%'+t1.name)

# print(hasattr(t,'name'))
# print(hasattr(t,'run'))