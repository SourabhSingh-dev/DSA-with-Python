def selection_Sort(arr):
    for i in range(0,len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
if __name__ == "__main__":
    sample_input =  [4,2,5,1,7,8,4]
    print(selection_Sort(sample_input))