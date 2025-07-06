def selection_sort(arr):
    for i in range(0,len(arr)):
        max_index = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i],arr[max_index] = arr[max_index],arr[i]
    return arr
if __name__ == "__main__":
    sample_input =  [4,2,5,1,7,8,4]
    print(selection_sort(sample_input))