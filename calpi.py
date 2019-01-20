from random import random
from time import perf_counter
darts = 10000*10000
hits = 0.0
start = perf_counter()
for i in range(1,darts+1):
    x,y = random(),random()
    dis = pow(x**2+y**2,0.5)
    if dis<=1:
        hits = hits+1
pi = 4*hits/darts
end = perf_counter()
dur = end - start
print('{0:.10f},{1}'.format(pi,dur))
