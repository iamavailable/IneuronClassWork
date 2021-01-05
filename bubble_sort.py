
def bubble_sort(lst):
    for i in range(len(lst)-1, 0 , -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


lst = [12,2,1,34,23,65,31,98,36,122]
bubble_sort(lst)
print(lst)