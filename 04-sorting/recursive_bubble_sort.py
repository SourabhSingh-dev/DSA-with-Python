def recursive_bubble_sort(arr,limit=None):
    n = len(arr)
    if limit is None:
        limit = len(arr)
    if limit == 1:
        return
    is_swap = False
    for i in range(0,limit-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            is_swap = True

    if is_swap == False:
        return
    recursive_bubble_sort(arr,limit-1)
arr = [4, 1, 3, 9, 7]
recursive_bubble_sort(arr)
print(arr)