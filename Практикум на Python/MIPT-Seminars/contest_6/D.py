from contextlib import contextmanager
import sys
import traceback
from io import StringIO


@contextmanager
def supresser(*types):
    try:
        yield
    except types:
        pass


@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from:
        msg, exc, trace = sys.exc_info()
        new_exc = type_to().with_traceback(trace)
        new_exc.args = exc.args
        raise new_exc


@contextmanager
def dumper(output):
    try:
        yield
    except Exception as e:
        err_str = traceback.format_exception_only(e.__class__, e)
        err_str[0] = err_str[0][:-1]
        err_str += traceback.format_exc().split('\n')
        output.write('\n'.join(err_str))


out = StringIO()

'''
with dumper(out):
    print('abc')
    a = 1 / 0
print(out.getvalue())
out.close()
'''

