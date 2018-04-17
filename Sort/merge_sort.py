def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_children = alist[:mid]
        right_children = alist[mid:]

        merge_sort(left_children)
        merge_sort(right_children)

        i, j, k = 0, 0, 0
        while i < len(left_children) and j < len(right_children):
            if left_children[i] < right_children[j]:
                alist[k] = left_children[i]
                i += 1
            else:
                alist[k] = right_children[j]
                j += 1
            k += 1
        while i < len(left_children):
            alist[k] = left_children[i]
            i += 1
            k += 1
        while j < len(right_children):
            alist[k] = right_children[j]
            j += 1
            k += 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
