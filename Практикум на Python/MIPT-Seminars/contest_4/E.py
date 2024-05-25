import time
import functools


def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        main_call = False
        if not wrapper.runs:
            wrapper.runs = True
            wrapper.calls = 0
            main_call = True
            wrapper.start = time.time()

        wrapper.calls += 1
        value = func(*args, **kwargs)

        if main_call:
            end = time.time()
            wrapper.last_time_taken = end - wrapper.start
            wrapper.runs = False
        return value
    wrapper.last_time_taken = 0.0
    wrapper.calls = 0
    wrapper.runs = False
    return wrapper


@profiler
def sleepy_recursion(num_calls):
    "I am a strange sleepy recursive function"
    time.sleep(1)
    if num_calls > 1:
        sleepy_recursion(num_calls - 1)

