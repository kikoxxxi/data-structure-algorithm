def shell_sort(alist):
    sublist_count = len(alist) // 2
    while sublist_count > 0:
        for start_point in range(sublist_count):
            gap_insertion_sort(start_point, alist, sublist_count)
        sublist_count //= 2


def gap_insertion_sort(start, alist, gap):
    for i in range(start + gap, len(alist), gap):
        tmp = alist[i]
        j = i - gap
        while alist[j] > tmp and j >= start:
            alist[j + gap] = alist[j]
            j -= gap
        alist[j + gap] = tmp


alist = [0, 0, 3, 2, 3, 2, 54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
