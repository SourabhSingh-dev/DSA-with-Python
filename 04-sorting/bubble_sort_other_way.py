def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
if __name__ == "__main__":
    sample_input =  [4,2,5,1,7,8,4]
    print(bubble_sort(sample_input))