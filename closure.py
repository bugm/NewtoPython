#闭包
#闭包函数三点：1、要有内嵌函数 2、内嵌函数中要引用外部函数的变量 3、外部函数以内嵌函数作为返回值
def createCounter():
    x = 0
    def counter():
        x = 1
        x += 2
        return x
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

x = [1,2,3]
print(x*2)
x*=5
print(x)