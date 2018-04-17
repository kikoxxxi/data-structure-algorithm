def binary_search(alist, item):
    low = 0
    high = len(alist) - 1
    while low <= high:
        mid = (low + high) // 2
        if alist[mid] == item:
            return "在列表中找到item: {} 的位置为：{} .".format(item, mid)
        elif alist[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return "没有在列表中找到item: {} ，但可插入位置为：{} .".format(item, low)


def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search_recursive(alist[:mid], item)
        else:
            return binary_search_recursive(alist[mid + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search_recursive(testlist, 3))
print(binary_search_recursive(testlist, 13))
