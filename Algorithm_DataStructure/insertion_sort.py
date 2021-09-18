import pandas as pd
import random as rd
from time import perf_counter_ns

A = list(range(0, 100))
rd.shuffle(A)

B = list(range(0, 200))
rd.shuffle(B)

# C = list(range(0, 3000))
# rd.shuffle(C)

# D = list(range(0, 4000))
# rd.shuffle(D)

# E = list(range(0, 5000))
# rd.shuffle(E)

# F = list(range(0, 6000))
# rd.shuffle(F)

# G = list(range(0, 7000))
# rd.shuffle(G)

# H = list(range(0, 8000))
# rd.shuffle(H)


inp = [A, B]

output = []


# basic insertion sort func with clock


def insertion(input_list):
    time_start = perf_counter_ns()
    j = 1
    while j < len(input_list):
        key = input_list[j]
        i = j - 1
        while i > -1 and input_list[i] > key:
            input_list[i + 1] = input_list[i]
            i -= 1
        input_list[i + 1] = key
        j += 1
    time_end = perf_counter_ns()
    time_span = time_end - time_start
    return time_span

# func to run throw dataframe and logging 'insertion' func


def insertion_df(input_df):
    i = 0
    n = len(input_df.index)
    while i < n:
        time_span = insertion(input_df["numbers"][i])
        input_df["time_span"][i] = time_span
        i += 1


# creation of df for input
data_count = []
data_list = []

n = 10
i = 1
j = 0
while j < n:
    count = i * 125
    data_count.append(count)
    temp_list = list(range(0, count))
    rd.shuffle(temp_list)
    data_list.append(temp_list)
    i *= 2
    j += 1
# 512k burnt my M1 (it was it the sun tho) opted for 64k max

data = {"count": data_count, "numbers": data_list,
        "time_span": list(range(0, n))}
# list for time_span as placeholder -> ugly but works :D

df = pd.DataFrame(data, index=list(range(0, n)))

insertion_df(df)
