from Node import Node


def my_tree(root, arr, left_idx, right_idx):
    if left_idx >= right_idx:
        return
    middle = (left_idx + right_idx) // 2
    key, data = arr[middle]

    root.insert(key, data)

    my_tree(root, arr, left_idx, middle)
    my_tree(root, arr, middle+1, right_idx)


arr = list(range(1, 20))
myMap = map(lambda x: [f"Ana{x:03d}", x], arr)
arr2 = list(myMap)

middle = len(arr2) // 2
key, data = arr2[middle]

root = Node(key, data)
my_tree(root, arr2, 0, len(arr2))

root.display()

# Missing time complexity
