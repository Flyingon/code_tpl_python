import time
import functools


def wrapper_cost():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args):
            t = time.time()
            print(f"{func.__name__} begin")
            res = await func(*args)
            print(f"{func.__name__} end, cost: {time.time() - t:.8f}s")
            return res

        return wrapped

    return wrapper
