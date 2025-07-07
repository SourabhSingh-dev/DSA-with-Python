def recursive_insertion_sort(arr,limit=None):
    if limit == None:
        limit = 1
    if limit >= len(arr):
        return
    key = arr[limit]
    j = limit - 1
    while  j >= 0 and arr[j] >= key :
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    recursive_insertion_sort(arr,limit+1)
arr = [4, 1, 3, 9, 7]
recursive_insertion_sort(arr)
print(arr)