A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if A[mid - 1] != target:
                return mid
            if mid - 1 < 0:
                return mid
            high = mid - 1
    return None

# print(find(A, 0))
















