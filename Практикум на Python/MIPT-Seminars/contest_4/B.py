import heapq


def merge_sorter(*args):
    iters = [iter(arg) for arg in args]
    values = []
    for num in range(len(iters)):
        try:
            val = next(iters[num])
        except StopIteration:
            continue
        values.append((val, num))
    heapq.heapify(values)
    while values:
        val, num = heapq.heappop(values)
        yield val
        try:
            new_val = next(iters[num])
        except StopIteration:
            continue
        heapq.heappush(values, (new_val, num))

