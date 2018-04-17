def selection_sort(alist):
    for i in range(len(alist)-1):
        min_tag=i
        for j in range(i,len(alist)):
            if alist[j]<alist[min_tag]:
                min_tag=j
        alist[min_tag],alist[i]=alist[i],alist[min_tag]
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)