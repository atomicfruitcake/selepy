'''!
@author atomicfruitcake

'''

def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(*args, **kwargs)
            result = func(*args, **kwargs)
            post(*args, **kwargs)
            return result
        return call
    return decorate

def trace_in(func, *args, **kwargs):
   print("Entering function")

def trace_out(func, *args, **kwargs):
   print("Leaving function")

@wrap(trace_in, trace_out)
def calc(x, y):
   return x + y


if __name__ == '__main__':
    print(calc(1, 2))