'''
 ***broken.py***
 def foo():
     return 1

 refrigerator


 raise TypeError(’I can\’t type!’)

 def bar():
     return 2
'''
import traceback


def force_load(file):
    with open(file + '.py', 'r') as input_file:
        code = input_file.readlines()
    functions = {}
    while code:
        try:
            exec(''.join(code), globals(), functions)
        except Exception as e:
            error = traceback.format_exc().split('\n')
            while not ' '.join(error[-1].split()).startswith('File'):
                error.pop(-1)
            try:
                str_no = int(error[-1].split()[3])
            except ValueError:
                str_no = int(error[-1].split()[3][:-1])
            code.pop(str_no - 1)
            functions = {}
        else:
            break
    return functions

'''
m = force_load('broken')
print(m['foo']())
print(m['bar']())
'''
