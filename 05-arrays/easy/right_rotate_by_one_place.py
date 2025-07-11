def right_rotate_by_one_place(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = temp
if __name__ == "__main__":
    sample_input = [1,2,3,4,5,6,7]
    right_rotate_by_one_place(sample_input)
    print(sample_input)