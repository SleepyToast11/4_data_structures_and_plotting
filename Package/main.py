import random
import time

from Package.Binary_search_tree import BNS
from Package.HTSC import HTSC
from Package.HTLP import HTLP
from Package.SL import SL

htsc = HTSC(30467)
htlp = HTLP(30467)
sl = SL()

bns = BNS()
bns[900] = 7

htlp[700] = 7
print(htlp[700])

input1 = input("1,2 or 3")
bns_time = []
htlp_time = []
htsc_time = []
sl_time = []
x_axis = []

for i in range(1, 10000):
    if input1 == 1:
        x_axis.append(i)
        time_start = time.time_ns()
        bns[(i + 1)] = random.randint(0,500)
        bns_time.append(time.time_ns() - time_start)

        time_start = time.time_ns()
        htlp[i] = random.randint(0,500)
        htlp_time.append(time.time_ns() - time_start)

        time_start = time.time_ns()
        sl[i] = random.randint(0,500)
        sl_time.append(time.time_ns() - time_start)

        time_start = time.time_ns()
        htsc[i] = random.randint(0, 500)
        htsc_time.append(time.time_ns() - time_start)

    else:
        bns[(i + 1)] = random.randint(0,500)
        htlp[i] = random.randint(0,500)
        sl[i] = random.randint(0,500)
        htsc[i] = random.randint(0, 500)
for i in range(1, 10000):
    if input1 == 2:
        x_axis.append(i)
        time_start = time.time_ns()
        print(bns[(i + 1)])
        bns_time.append(time.time_ns() - time_start)

        time_start = time.time_ns()
        print(htlp[i])
        htlp_time.append(time.time_ns() - time_start)

        time_start = time.time_ns()
        print(sl[i])
        sl_time.append(time.time_ns() - time_start)

        time_start = time.time_ns()
        print(htsc[i])
        htsc_time.append(time.time_ns() - time_start)

for i in range(1, 10000):
    del bns[(i + 1)]
    del htlp[i]
    del sl[i]
    del htsc[i]
    print(i)

input("  ")
