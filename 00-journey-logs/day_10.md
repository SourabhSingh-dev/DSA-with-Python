# 🗓️ Day 10 – 08/08/2025

### 📍 Status: ✅ Completed

---

## ✅ What I did today:

* 📌 **Topic:** Arrays – Two Pointer Technique (In-Place Partitioning)
  - ✅ Solved `Sort Array By Parity` from LeetCode
  - ✅ Explored multiple approaches:
    - List concatenation (O(n) time, O(n) space)
    - Two-pointer with many branches (O(n) time, O(1) space)
    - Corrected minimal-branch two-pointer (O(n) time, O(1) space, faster in Python)
  - ✅ Learned when “in-place” optimizations can be slower in Python due to branching overhead
  - ✅ Practiced dry runs to confirm pointer movement logic
  - ✅ Maintained clean Notion notes with code comparisons

* 📘 **Resources:**
  - LeetCode Problem: Sort Array By Parity
  - Self-debugging + pattern refinement through discussion

---

## 💻 Problem Solved:
- `sort_array_by_parity.py` ✅ (Two Pointer, In-Place Partitioning)

---

## 🧠 Reflections:
* Realized that **algorithmic complexity** isn’t the only factor — fewer branches and simpler loops often run faster in Python
* Understood the **pointer movement discipline** in partitioning problems to avoid skipping elements
* Caught the logical swap-condition bug in one version and fixed it to only swap when needed
* Learned that the most “memory-optimal” solution isn’t always the most runtime-optimal in Python

---

## 🔄 Next Up:
* Continue with more **Two Pointer** partitioning problems
* Explore similar parity/condition-based rearrangement tasks
* Track performance differences between Python and lower-level implementations for the same logic

---
