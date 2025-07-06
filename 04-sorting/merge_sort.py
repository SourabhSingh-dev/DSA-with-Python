def merge_array(left,right):
    i,j = 0,0
    n,m = len(left),len(right)
    res = []
    while i<n and j<m:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i<n:
        while i<n:
            res.append(left[i])
            i+= 1
    if j<m:
        while j<m:
            res.append(right[j])
            j += 1
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    mid = n//2
    left_arr = arr[ : mid]
    right_arr = arr[mid : ]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left,right)

if __name__ == "__main__":
    sample_input = [3,1,6,2,4,8,7]
    print("Output : ",merge_sort(sample_input))
