def bubble_sort(arr):
    i = len(arr) - 1
    j = 0
    while (i>j):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        i -= 1
        j = 0
    return arr
if __name__ == "__main__":
    sample_input =  [4,2,5,1,7,8,4]
    print(bubble_sort(sample_input))