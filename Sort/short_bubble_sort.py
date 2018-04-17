def bubble_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1, i, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


def short_bubble_sort(alist):
    swap = True
    i=0
    while i < (len(alist) - 1) and swap:
        swap=False
        for j in range(len(alist) - 1, i, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                swap = True
        i+=1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
short_bubble_sort(alist)
print(alist)
