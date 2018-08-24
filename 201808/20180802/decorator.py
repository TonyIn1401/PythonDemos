# _*_ coding: utf-8 _*_
import functools

def log(func):
    @functools.wraps(func)
    def wapper(*args, **kw):
        print('call {}'.format(func.__name__))
        return func(*args, **kw)
    return wapper

def logwithtxt(strwords):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print("{} {}".format(strwords, func.__name__))
            return func(*args, **kw)
        return wapper
    return decorator


#@log
@logwithtxt("log with text")
def wr():
    print("Hello world!")

wr()
print(wr.__name__)
