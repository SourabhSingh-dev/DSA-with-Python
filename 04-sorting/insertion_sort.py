def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
if __name__ == "__main__":
    sample_input =  [4,2,5,1,7,8,4]
    print(insertion_sort(sample_input))