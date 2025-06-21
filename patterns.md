## 🧠 Digital Root Trick

**Definition:**  
The digital root is the single-digit result of repeatedly summing the digits of a number until one digit remains.

**When to Use:**  
✔️ Use when you're asked to keep summing digits until one digit is left — often in math-based number problems.

**Key Tricks:**  
- Formula: `1 + (num - 1) % 9` (handles 0 separately)
- Avoids all loops or recursion — pure O(1) solution

**Example Problems:**
- [Add Digits (LeetCode #258)](https://leetcode.com/problems/add-digits/)

**My Solved Problems:**
- ✅ `add_digits.py` – `01-numbers/`
- ✅ `add_digits_betterway.py` – `betterway/`
