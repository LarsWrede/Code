from Node import Node
from time import perf_counter_ns
import pandas as pd

# function to balance the binary search tree


def new_tree(self, arr, left_index, right_index):
    time_start = perf_counter_ns()
    while left_index >= right_index:
        time_end = perf_counter_ns()
        time_span = time_end - time_start
        print(time_span)
        return time_span
    middle = (left_index + right_index) // 2
    key, data = arr[middle]

    root.insert(key, data)

    new_tree(self, arr, left_index, middle)
    new_tree(self, arr, middle+1, right_index)


# create array
n = 11

arr = list(range(1, n))
mapping = map(lambda x: [f'Tom{x:02d}', x], arr)
final_arr = list(mapping)

print(final_arr)

middle = len(final_arr) // 2
key, data = final_arr[middle]

root = Node(key, data)
new_tree(root, final_arr, 0, len(final_arr))

data_count = []
data_list = []

data = {"count": data_count, "numbers": data_list,
        "time_span": list(range(0, n))}

# df = pd.DataFrame(data, index=list(range(0, n)))

root.display()
# print(time_span)
