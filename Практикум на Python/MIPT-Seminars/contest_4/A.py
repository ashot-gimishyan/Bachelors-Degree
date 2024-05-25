def pascal_triangle():
    arr = [1]
    while True:
        for i in arr:
            yield i
        arr.append(0)
        newarr = [arr[i - 1] + arr[i] for i in range(0, len(arr))]
        arr = newarr
