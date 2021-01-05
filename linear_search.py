
# def linear_search(lst, n):
#     pos = 0
#     for i in range(len(lst)):
#         if lst[i] == n:
#             pos = i
#             print("Found at",pos+1)
#             return True
#
#     return False
#
# arr = [12,2,1,34,23,65,31,98,36,122]
#
# n=31
# linear_search(arr, n)


# def binary_search(lst, n):
#     pos = 0
#     l = 0
#     u = len(lst)-1
#
#     while l <= u:
#         mid = (l + u) // 2
#         if lst[mid] == n:
#             pos= mid
#             print("Found at ", pos+1)
#             return True
#         else:
#             if lst[mid] < n:
#                 l = mid+1
#             else:
#                 u = mid-1
#
#     return False
#
# lst = [1,2,3,4,5,23,45,56,67,78,89,90]
# n=56
# binary_search(lst, n)