"""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2.
Constraints:
1  <=  a.size(), b.size()  <=  105
-109  <=  a[i] , b[i]  <=  109
"""
def merged_array(a,b):
    i,j = 0,0
    n,m = len(a),len(b)
    res = []
    prev = None
    while i < n and j < m:
        if a[i] == b[j]:
            prev = a[i]
            res.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            prev = b[j]
            res.append(b[j])
            j += 1
        else:
            prev = a[i]
            res.append(a[i])
            i += 1
    while i < n:
        if a[i] != prev:
            prev = a[i]
            res.append(a[i])
        i += 1
    while j < m:
        if b[j] != prev:
            prev = b[j]
            res.append(b[j])
        j += 1
    return res
if __name__ == "__main__":
    sample_input_1 = [1, 2, 2, 3]
    sample_input_2 = [1, 4]
    print("Output : ",merged_array(sample_input_1,sample_input_2))

## Will visit this question later