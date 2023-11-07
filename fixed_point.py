# A = [-10, -5, 0, 3, 7]
#
# def binary_search(array):
#     low = 0
#     high = len(array) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if array[mid] == mid:
#             return array[mid]
#         elif array[mid] > mid:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# print(binary_search(A))
# print(len(A) - 1)

import time

A = [-10, -5, 0, 3, 7]

def binary_search(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == mid:
            return array[mid]
        elif array[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binary_search(A))


def linear_search(array):
    for i in range(len(array)):
        if array[i] == i:
            return i
    return None

print(linear_search(A))



A = [-10, -5, 0, 3, 7]






























