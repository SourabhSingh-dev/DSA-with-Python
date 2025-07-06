def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                is_swap = True
        if is_swap == False:
            return arr
    return arr
if __name__ == "__main__":
    sample_input =  [4 ,1 ,3 ,9 ,7]
    print(bubble_sort(sample_input))