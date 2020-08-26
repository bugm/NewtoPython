import time,functools
def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        start = time.time()
        result =  func(*args,**kw)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end - start))
        return result
    return wrapper

def log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    #time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

@log('123')
def f():
    print('f now')
    return 123

x = f()
print(x)
