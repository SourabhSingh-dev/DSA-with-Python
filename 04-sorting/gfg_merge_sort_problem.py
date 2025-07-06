"""
Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Input: arr[] = [1, 3 , 2]
Output: [1, 2, 3]
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105
"""

def merge(arr,l,m,r):
    sub_arr1 = arr[l:m+1]
    sub_arr2 = arr[m+1:r+1]
    res = []
    i,j = 0,0
    a,b = len(sub_arr1),len(sub_arr2)
    while i<a and j <b:
        if sub_arr1[i] < sub_arr2[j]:
            res.append(sub_arr1[i])
            i+=1
        else:
            res.append(sub_arr2[j])
            j+=1
    if i<a:
        while i<a:
            res.append(sub_arr1[i])
            i += 1
    if j < b:
        while j < b:
            res.append(sub_arr2[j])
            j += 1
    arr[l:r+1] = res
def mergeSort(arr,l,r):
    if l >= r:
        return
    mid = (l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)
arr = [10,3,7,5,9,2,6]
mergeSort(arr,1,5)
print(arr)