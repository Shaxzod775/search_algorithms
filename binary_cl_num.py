# A = [1, 2, 4, 5, 6, 6, 8, 9]

# def find_closest_num(array, target):
#     global min_diff_right, min_diff_left
#     min_diff = float('inf')
#     low = 0
#     high = len(array) - 1
#     closest_num = None
#
#     if len(array) == 0:
#         return None
#     if len(array) == 1:
#         return array[0]
#
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if mid + 1 < len(array):
#             min_diff_right = abs(array[mid + 1] - target)
#         if mid > 0:
#             min_diff_left = abs(array[mid - 1] - target)
#
#         if min_diff_right < min_diff:
#             min_diff = min_diff_right
#             closest_num = array[mid + 1]
#
#         if min_diff_left < min_diff:
#             min_diff = min_diff_left
#             closest_num = array[mid - 1]
#
#         if array[mid] < target:
#             low = mid + 1
#         elif array[mid] > target:
#             high = mid - 1
#         else:
#             return array[mid]
#
#     return closest_num
#
# # A = [2, 5, 6, 7, 8, 8, 9]
# A = [1, 2, 4, 5, 6, 6, 8, 9]
# print(find_closest_num(A, 3))












# def find_closest_num(array, target):
#     global min_right_diff, min_left_diff
#     low = 0
#     high = len(array) - 1
#     min_diff = float("inf")
#     closest_num = None
#
#     if len(array) == 0:
#         return None
#     if len(array) == 1:
#         return array[0]
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if mid + 1 < len(array):
#             min_right_diff = abs(array[mid + 1] - target)
#         if mid > 0:
#             min_left_diff = abs(array[mid - 1] - target)
#
#         if min_right_diff < min_diff:
#             min_diff = min_right_diff
#             closest_num = array[mid + 1]
#
#         if min_left_diff < min_diff:
#             min_diff = min_left_diff
#             closest_num = array[mid - 1]
#
#         if array[mid] < target:
#             low = mid + 1
#         elif array[mid] > target:
#             high = mid - 1
#         else:
#             return array[mid]
#
#     return closest_num
#
# A = [1, 2, 4, 5, 6, 6, 8, 9]
# print(find_closest_num(A, 0))





# def find_closest_num(A, target):
#     global min_right_diff, min_left_diff
#     low = 0
#     high = len(A) - 1
#     min_diff = float('inf')
#     closest_number = None
#
#     if len(A) == 0:
#         return None
#     if len(A) == 1:
#         return A[0]
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if mid + 1 < len(A):
#             min_right_diff = abs(A[mid + 1] - target)
#         if mid > 0:
#             min_left_diff = abs(A[mid - 1] - target)
#
#         if min_right_diff < min_diff:
#             min_diff = min_right_diff
#             closest_number = A[mid + 1]
#
#         if min_left_diff < min_diff:
#             min_diff = min_left_diff
#             closest_number = A[mid - 1]
#
#         if A[mid] > target:
#             high = mid - 1
#         elif A[mid] < target:
#             low = mid + 1
#         else:
#             return A[mid]
#
#     return closest_number



# A = [1, 2, 4, 5, 6, 6, 8, 9]
# print(find_closest_num(A, 7))














def find_closest_number(array, target):
    global min_right_diff, min_left_diff
    low = 0
    high = len(array) - 1
    min_diff = float('inf')
    closest_number = None

    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(array):
            min_right_diff = abs(array[mid + 1] - target)
        if mid > 0:
            min_left_diff = abs(array[mid - 1] - target)

        if min_right_diff < min_diff:
            min_diff = min_right_diff
            closest_number = array[mid + 1]

        if min_left_diff < min_diff:
            min_diff = min_left_diff
            closest_number = array[mid - 1]

        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            return array[mid]

    return closest_number


A = [1, 2, 4, 5, 6, 6, 8, 9]
print(find_closest_number(A, 5))














