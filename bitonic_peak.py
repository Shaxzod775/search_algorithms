

# def find_highest_number(A):
#     low = 0
#     high = len(A) - 1
#
#     if len(A) < 3:
#         return None
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         mid_left = A[mid - 1] if mid - 1 > 0 else float('-inf')
#         mid_right = A[mid + 1] if mid + 1 < len(A) else float('inf')
#
#         if mid_left < A[mid] and mid_right > A[mid]:
#             low = mid + 1
#         elif mid_left > A[mid] and mid_right < A[mid]:
#             high = mid - 1
#         elif mid_left < A[mid] and mid_right < A[mid]:
#             return A[mid]
#         else:
#             return None
#
# print(find_highest_number(A2))


# def find_highest_number(A):
#     low = 0
#     high = len(A) - 1
#
#     if len(A) < 3:
#         return None
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         mid_left = A[mid - 1] if mid - 1 > 0 else float('-inf')
#         mid_right = A[mid + 1] if mid + 1 < len(A) else float('inf')
#
#         if mid_left > A[mid] and mid_right < A[mid]:
#             high = mid - 1
#         elif mid_left < A[mid] and mid_right > A[mid]:
#             low = mid + 1
#         elif mid_left < A[mid] and mid_right < A[mid]:
#             return A[mid]
#         else:
#             return None


# # 5
# A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# # 4
# A1 = [1, 2, 3, 4, 1]
# # 6
# A2 = [1, 6, 5, 4, 3, 2, 1]
# print(find_highest_number(A2))







