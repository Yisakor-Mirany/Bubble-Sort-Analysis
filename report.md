# Bubble Sort Analysis Report

**Module:** AD312 Intermediate Development 2  
**Language:** Python 3

---

## 1. Code Summary

Two functions are implemented in `bubble_sort.py`:

### `bubble_sort_basic(lst)`

The basic version uses two nested loops.  The outer loop runs `n - 1` times,
where `n` is the length of the list.  The inner loop walks from the start of
the list to the end of the currently unsorted portion, comparing each adjacent
pair and swapping them when they are out of order.

Every pass is always executed in full, regardless of whether the list becomes
sorted before all passes are complete.  This means the basic version always
performs exactly **n(n-1)/2** comparisons.

### `bubble_sort_optimized(lst)`

The optimized version is identical to the basic version except for one
addition: a boolean flag called `swapped`.  At the start of each pass the flag
is set to `False`.  If any swap is made during the pass, the flag is set to
`True`.  After the inner loop finishes, if `swapped` is still `False`, the list
is already in sorted order and the outer loop breaks immediately.

This single change dramatically reduces the number of passes needed for
nearly-sorted or already-sorted input.

Both functions operate on a **copy** of the input list and return a new list,
leaving the original unchanged.

---

## 2. Test Cases

The test suite in `test_bubble_sort.py` covers the following scenarios.  Every
test is run against both the basic and optimized implementations to confirm they
produce identical, correct results.

| # | Test Case | Input Example | Expected Output | Purpose |
|---|-----------|---------------|-----------------|---------|
| 1 | Random list | `[47, 5, 83, 12, 61]` | `[5, 12, 47, 61, 83]` | General correctness on unsorted data. |
| 2 | Already sorted | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | Verifies no corruption on sorted input; best case for optimized version. |
| 3 | Descending list | `[9, 7, 5, 3, 1]` | `[1, 3, 5, 7, 9]` | Worst-case input — every element must move. |
| 4 | All identical values | `[4, 4, 4, 4, 4]` | `[4, 4, 4, 4, 4]` | No swaps should occur; result equals input. |
| 5 | Empty list | `[]` | `[]` | Edge case — algorithm must not raise an error. |
| 6 | Single element | `[99]` | `[99]` | Edge case — trivially sorted, no comparisons needed. |
| 7 | Negative numbers | `[-5, 3, -1, 0, 7]` | `[-5, -3, -1, 0, 3, 7]` | Correctness with values below zero. |
| 8 | Two elements (swap) | `[2, 1]` | `[1, 2]` | Minimal swapping case. |
| 9 | Two elements (no swap) | `[1, 2]` | `[1, 2]` | Minimal no-swap case. |
| 10 | Input not mutated | `[3, 1, 4, 1, 5]` | Original unchanged | Both functions must copy, not sort in place. |

---

## 3. Time Complexity Analysis

Time complexity describes how the number of operations grows as the input size
`n` increases.

### Basic Bubble Sort

| Case | Complexity | Explanation |
|------|-----------|-------------|
| **Best case** | O(n²) | Even if the list is already sorted, all `n-1` passes run to completion. The total number of comparisons is always n(n-1)/2. |
| **Average case** | O(n²) | For a randomly ordered list, roughly half of all possible swaps are needed, which still scales quadratically. |
| **Worst case** | O(n²) | A fully reversed list requires the maximum number of swaps. The two nested loops each run approximately `n` times, giving O(n²). |

### Optimized Bubble Sort

| Case | Complexity | Explanation |
|------|-----------|-------------|
| **Best case** | **O(n)** | On an already-sorted list, the first pass makes zero swaps. The `swapped` flag triggers an immediate exit after just `n-1` comparisons — one full pass. |
| **Average case** | O(n²) | On random data the early exit rarely triggers, so performance is still quadratic on average. |
| **Worst case** | O(n²) | A fully reversed list produces at least one swap on every pass, so all `n-1` passes run to completion — same as the basic version. |

**Key takeaway:** the optimized version's advantage is narrow but meaningful.
For data that is already sorted or very nearly sorted, it can be significantly
faster.  For random or reversed data the improvement is negligible.

---

## 4. Space Complexity Analysis

Both implementations use **O(1)** auxiliary space (constant extra memory).

The algorithm sorts by swapping elements within the list.  It does not create
any additional data structures whose size depends on `n`.  The only extra
variables used are loop counters (`i`, `j`) and, in the optimized version, the
boolean flag `swapped` — all fixed in size regardless of how large the input
is.

> **Note:** Both functions in this project create a copy of the input list
> (`data = lst[:]`) before sorting.  This copy is O(n) space, but it is a
> design choice to protect the caller's data, not a requirement of the
> algorithm itself.  A purely in-place implementation would use O(1) total
> space.

---

## 5. Why Bubble Sort Is Stable

A sorting algorithm is called **stable** if it preserves the original relative
order of elements that are equal in value.

Bubble Sort is stable because its swap condition is **strictly greater than**
(`>`), not greater than or equal to (`>=`):

```python
if data[j] > data[j + 1]:
    data[j], data[j + 1] = data[j + 1], data[j]
```

When two adjacent elements are equal (`data[j] == data[j + 1]`), the condition
is `False` and no swap takes place.  Equal elements therefore never overtake
each other during the sort.  After all passes are complete, two elements with
the same value appear in the output in the same left-to-right order that they
appeared in the input.

This property matters in practice when sorting objects by one field and the
objects also carry other data.  For example, if student records are first sorted
by name and then by grade using a stable sort, students with the same grade
remain in alphabetical order within that grade group.

---

## 6. Observations on the Optimized Version

1. **Best-case improvement is dramatic.**  For an already-sorted list of 1,000
   elements, the basic version still performs 499,500 comparisons.  The
   optimized version performs only 999 comparisons (one pass) before exiting.
   This is roughly a 500× reduction in work for this specific case.

2. **Average and worst-case improvement is negligible.**  On random or reversed
   data the `swapped` flag is almost never still `False` at the end of a pass,
   so the outer loop runs through all `n-1` passes just like the basic version.
   The flag itself adds a tiny constant overhead per pass.

3. **Nearly-sorted data is a practical middle ground.**  Real-world data (log
   files with a late entry, or a leaderboard with one score updated) is often
   "almost sorted."  The optimized version can exit after just a few passes
   instead of all `n-1`, making it noticeably faster in these common scenarios.

4. **The change is minimal.**  Adding the `swapped` flag requires only three
   extra lines of code but can transform the best-case complexity from O(n²)
   to O(n).  This illustrates how a small, targeted improvement can have a
   significant effect on performance for certain inputs.

5. **Bubble Sort is still not competitive for large datasets.**  Even with the
   optimization, both versions are O(n²) in the average and worst cases.
   Algorithms such as Merge Sort and Quick Sort achieve O(n log n) average
   performance and are preferred for large or unknown inputs.  Bubble Sort's
   main value is its simplicity as a teaching example.

---

*End of report.*
