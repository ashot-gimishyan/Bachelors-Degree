def years(start, stop):
    for i in range(start, stop+1):
        i = str(i)
        i = list(i)
        i = [int(n) for n in i]
        for j in range(0, 10):
            if i.count(j) == 3:
                for k in i:
                    print(k,end="")
                print()
                break



stt = int(input())
stp = int(input())

years(stt,stp)