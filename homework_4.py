
def search_in_matrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    if n == 0:
        return False
    i = 0
    j = n - 1
    while i < m and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] < target:
            i = i + 1
        else:
            j = j - 1
    return [-1, -1]


values = [
[1, 4, 7, 12, 15, 1000],
[2, 5, 19, 31, 32, 1001],
[3, 8, 24, 33, 35, 1002],
[40, 41, 42, 44, 45, 1003],
[99, 100, 102, 103, 106, 128, 1004]             # this has 7 numbers, rest have six
]


print(search_in_matrix(values, 8))                  # should return [2, 1]
print(search_in_matrix(values, 42))                 # should return [3, 2]
print(search_in_matrix(values, 106))                # should return [4, 3]
print(search_in_matrix(values, 15))                 # should return [0, 4]
print(search_in_matrix(values, 102))                # should return [4, 2]
print(search_in_matrix(values, 6))                  # should return [-1, -1]
print(search_in_matrix(values, 17))                 # should return [-1, -1]


# def search_in_matrix(matrix, target):
#     if not matrix or not matrix[0]:
#         return ValueError
#
#     j = len(matrix) - 1
#     for row in matrix:
#         while row[j] > target:
#             j = j - 1
#             if j == 1:
#                 return [-1, -1]
#         if row[j] == target:
#             return [j, j]
#     return False
#
#
# values = [
# [1, 4, 7, 12, 15, 1000],
# [2, 5, 19, 31, 32, 1001],
# [3, 8, 24, 33, 35, 1002],
# [40, 41, 42, 44, 45, 1003],
# [99, 100, 102, 103, 106, 128, 1004]
# ]
#
#
# print(search_in_matrix(values, 8))                  # should return [2, 1]
# print(search_in_matrix(values, 42))                 # should return [3, 2]
# print(search_in_matrix(values, 106))                # should return [4, 3]
# print(search_in_matrix(values, 15))                 # should return [0, 4]
# print(search_in_matrix(values, 6))                  # should return [-1, -1]
# print(search_in_matrix(values, 17))                 # should return [-1, -1]
# print(search_in_matrix(values, 102))               # should return [4, 6]
