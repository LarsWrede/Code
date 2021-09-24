#!/usr/bin/env python
# coding: utf-8


from time import perf_counter_ns
from LinkedList import LinkedList
from random import randrange

i = 10
while i <= 100000:
    test = LinkedList()

    for j in (range(i)):
        test.add(j)

    time_start = perf_counter_ns()
    for k in range(100):
        test.at(randrange(i))

    time_end = perf_counter_ns()
    time_span = time_end - time_start
    time_in_sec_10000 = time_span / 1000000000
    print(f"i: {i} takes {time_in_sec_10000} Seconds")

    i = 10*i
