import _bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

_bisect.bisect_left(A, 401)
_bisect.bisect_right(A, 108)
_bisect.insort_left(A, 285)
_bisect.insort_right(A, 108)
print(A)





























