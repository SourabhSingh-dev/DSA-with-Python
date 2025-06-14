def reverse(n):
    sign = -1 if n<0 else 1
    n = abs(n)
    reverse = int(str(n)[: : -1])
    final_ans = reverse*sign
    if (-2**31 <= final_ans <= 2**31 - 1):
        return final_ans
    else :
        return 0
        
input_num = int(input("Enter the number : "))
num = input_num
reverse_num = reverse(num)
print(reverse_num)   