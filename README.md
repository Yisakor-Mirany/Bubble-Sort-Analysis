# Bubble Sort Analysis

**AD312 Intermediate Development 2**

---

## What This Project Does

This project implements and tests the **Bubble Sort** algorithm in Python.  
Two versions are provided:

| Version | Description |
|---------|-------------|
| `bubble_sort_basic` | The classic, straightforward implementation. |
| `bubble_sort_optimized` | An improved version that exits early when the list is already sorted. |

A full test suite covers six different input scenarios, and a written report
analyses the time and space complexity of both versions.

---

## How Bubble Sort Works

Bubble Sort is one of the simplest sorting algorithms.  It works by repeatedly
stepping through a list, comparing each pair of neighbouring elements, and
swapping them if they are in the wrong order.

After every complete pass, the largest unsorted element has "bubbled" to its
correct position at the end of the unsorted portion of the list.  The algorithm
repeats this process until no more swaps are needed.

**Step-by-step example** — sorting `[5, 3, 1, 4, 2]`:

```
Pass 1:  [3, 1, 4, 2, 5]   → 5 is now in its final position
Pass 2:  [1, 3, 2, 4, 5]   → 4 is now in its final position
Pass 3:  [1, 2, 3, 4, 5]   → sorted!
```

The **optimized version** adds a flag (`swapped`) that is set to `False` at
the start of each pass.  If the whole pass completes without a single swap, the
list is already sorted and the algorithm stops immediately — saving unnecessary
work.

---

## Project Files

```
bubble-sort-analysis/
├── bubble_sort.py        # Algorithm implementations
├── test_bubble_sort.py   # Pytest test suite
├── report.md             # Analysis and write-up
└── README.md             # This file
```

---

## Requirements

- Python 3.8 or later  
- [pytest](https://docs.pytest.org/) (install with `pip install pytest`)

---

## How to Run the Program

Run `bubble_sort.py` directly to see a quick demonstration:

```bash
python bubble_sort.py
```

**Example output:**

```
Original list   : [47, 12, 83, 5, 61, 28, 90, 34, 17, 56]
Basic sort      : [5, 12, 17, 28, 34, 47, 56, 61, 83, 90]
Optimized sort  : [5, 12, 17, 28, 34, 47, 56, 61, 83, 90]

Already sorted  : [1, 2, 3, 4, 5]
Basic sort      : [1, 2, 3, 4, 5]
Optimized sort  : [1, 2, 3, 4, 5]
```

---

## How to Run the Tests

From the project directory, run:

```bash
python -m pytest test_bubble_sort.py -v
```

The `-v` flag gives verbose output, showing each test case by name.

**Expected output (all tests passing):**

```
test_bubble_sort.py::TestBubbleSort::test_random_list[basic] PASSED
test_bubble_sort.py::TestBubbleSort::test_random_list[optimized] PASSED
test_bubble_sort.py::TestBubbleSort::test_already_sorted[basic] PASSED
test_bubble_sort.py::TestBubbleSort::test_already_sorted[optimized] PASSED
...
============ 23 passed in 0.12s ============
```

---

## How to Use the Functions in Your Own Code

```python
from bubble_sort import bubble_sort_basic, bubble_sort_optimized

numbers = [64, 25, 12, 22, 11]

sorted_basic     = bubble_sort_basic(numbers)
sorted_optimized = bubble_sort_optimized(numbers)

print(sorted_basic)      # [11, 12, 22, 25, 64]
print(sorted_optimized)  # [11, 12, 22, 25, 64]

# The original list is never modified
print(numbers)           # [64, 25, 12, 22, 11]
```

---

## Author

Submitted for **AD312 Intermediate Development 2**.
