#🔁 DSA Revision Insights – Quick Ref

Short, sharp reminders of key learnings from each day. One-liners only.

##📅 14/06/2025

1.Reverse Integer: Handle negatives with abs(n), reapply sign. Check best submissions after solving.

2.If you don't want to check palindrome using slicing then reverse the number and compare the reversed number with the original number.

Related Files : 01-numbers/reverse_integer_betterway.py and 01-numbers/reverse_integer.py

🔢 Evenly Dividing Digits: Skip digit 0 to avoid division error.

##📅 21/06/2025
### 🔁  Add Digits (LeetCode #258)

- **Concept:** Learned the concept of the *Digital Root* — the single-digit result of repeatedly summing the digits of a number.
- **Optimized Formula:**  
  ```python
  1 + (num - 1) % 9

- *Digital Root* - 38 --> 3 + 8 --> 11 ---> 1+1 --> 2
so the digital root of 38 is 2.