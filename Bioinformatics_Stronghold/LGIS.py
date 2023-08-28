### Longest increasing subsequence ###

def BinarySearch(sorted_list,x):
    bot = 0
    top = len(sorted_list) -1
    while bot < top:
        mid = (top + bot) // 2
        if x > sorted_list[mid]:
            bot = mid + 1
        else:
            top = mid
    return top

def FindLS(perm):
    upLS = []
    for num in perm:
        if len(upLS) == 0 or upLS[len(upLS)-1] < num:
            upLS.append(num)
        else:
            upLS[BinarySearch(upLS,num)] = num
    return upLS

perm = [1,5,4,2,3,8,6,7,9,3,4,5]
print(FindLS(perm))