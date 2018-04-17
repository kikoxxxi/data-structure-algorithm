def insertion_sort(alist):
    for i in range(1, len(alist)):
        tmp = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > tmp:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = tmp


alist = [54, 1, 1, 2, 7, 2, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
