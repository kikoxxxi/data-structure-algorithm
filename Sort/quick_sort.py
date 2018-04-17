def quick_sort(alist):
    return quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while alist[left_mark] <= pivot_value and left_mark <= right_mark:
            left_mark += 1
        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            alist[right_mark], alist[left_mark] = alist[left_mark], alist[right_mark]
    alist[right_mark], alist[first] = alist[first], alist[right_mark]
    return right_mark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist)
print(alist)
