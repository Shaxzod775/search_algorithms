# 1
# def binary_search_iterative(array, target):
#     low = 0
#     high = len(array) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if array[mid] == target:
#             return True
#         elif array[mid] > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return False

# def binary_search_recursive(array, target, low, high):
#     if low > high:
#         return False
#     else:
#         mid = (low + high) // 2
#         if array[mid] == target:
#             return True
#         elif mid > target:
#             return binary_search_recursive(array, target, low, mid-1)
#         else:
#             return binary_search_recursive(array, target, mid+1, high)
#
# data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# target = 13
# print(binary_search_recursive(data, target, 0, len(data) - 1))





# def linear_search(array, target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return True
#     return False
#
# data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# target = 11
# print(linear_search(data, target))

# 2

# def closest_number(array, target):
#     global min_right_diff, min_left_diff
#     low = 0
#     high = len(array) - 1
#     min_diff = float('inf')
#     closest_number = None
#
#     if len(array) == 0:
#         return None
#     if len(array) == 1:
#         return array[0]
#
#     while low <= high:
#         mid = (low + high) // 2
#         if mid + 1 < len(array):
#             min_right_diff = abs(array[mid + 1] - target)
#         if mid - 0:
#             min_left_diff = abs(array[mid - 1] - target)
#
#         if min_right_diff < min_diff:
#             min_diff = min_right_diff
#             closest_number = array[mid + 1]
#
#         if min_left_diff < min_diff:
#             min_diff = min_left_diff
#             closest_number = array[mid - 1]
#
#         if array[mid] > target:
#             high = mid - 1
#         elif array[mid] < target:
#             low = mid + 1
#         else:
#             return array[mid]
#
#     return closest_number
#
# A = [1, 2, 4, 5, 6, 6, 8, 9]
# print(closest_number(A, 3))

# 3

# def find_fixed_point_binary(array):
#     low = 0
#     high = len(array) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if array[mid] == mid:
#             return array[mid]
#         elif array[mid] > mid:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# A = [-10, -5, 0, 3, 7]
# print(find_fixed_point_binary(A))
#
# def find_fixed_point_linear(array):
#     for i in range(len(array)):
#         if array[i] == i:
#             return i
#     return None
#
#
# print(find_fixed_point_linear(A))


