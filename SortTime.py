import SortLib
import time
import random
N = int(input())
Massiv = [random.randint(1,1000000) for i in range(N)]
Start = time.time()
SortLib.quick_sort(Massiv, 0, N-1)
Finish = time.time()
Res_msec = (Finish - Start)*1000
print(Res_msec)
