A = [4, 5, 6, 7, 1, 2, 3]

def find_1(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid
    return low

print(find_1(A))








