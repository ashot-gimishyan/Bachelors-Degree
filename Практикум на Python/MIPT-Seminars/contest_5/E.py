import import_me


def get_all_functions():
    res = []
    for f in dir(import_me):
        if callable(getattr(import_me, f)):
            res.append(f)
    return res
