def second_largest(arr):
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(0,len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return largest,second_largest
if __name__ == "__main__":
    print("Output : ",second_largest([23,44,11,42,87,91]))
    