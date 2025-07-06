def partition(arr,low,high):
    pivot = arr[low]
    i,j = low,high
    while True:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot :
            j -= 1
        if i>j:
            break
        arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        p_index = partition(arr,low,high)
        quick_sort(arr,low,p_index-1)
        quick_sort(arr,p_index+1,high)
arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr) 
