"""
bubble_sort.py
AD312 Intermediate Development 2

Implements basic and optimized Bubble Sort algorithms.
"""


def bubble_sort_basic(lst):
    """
    Sort a list of integers in ascending order using basic Bubble Sort.

    The algorithm repeatedly steps through the list, compares adjacent
    elements, and swaps them if they are in the wrong order.  Every full
    pass 'bubbles' the largest unsorted element to its correct position
    at the end of the list.  The process repeats for n-1 passes, where
    n is the length of the list.

    Time complexity : O(n^2) — always performs all passes regardless of input.
    Space complexity: O(1)  — sorts in place.

    Parameters
    ----------
    lst : list[int]
        The list to sort.  The original list is NOT modified.

    Returns
    -------
    list[int]
        A new list containing the same integers sorted in ascending order.
    """
    data = lst[:]          # work on a copy so the original stays unchanged
    n = len(data)

    for i in range(n - 1):
        # After pass i, the (i+1) largest elements are already in place
        # at the end of the list, so we only need to go up to index n-1-i.
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                # Swap the two adjacent elements
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def bubble_sort_optimized(lst):
    """
    Sort a list of integers in ascending order using optimized Bubble Sort.

    This version adds an early-exit flag: if a complete pass through the
    list produces zero swaps, the list is already sorted and the algorithm
    stops immediately.  This gives a best-case time complexity of O(n)
    for already-sorted input (only one pass is needed to confirm the list
    is in order).

    Time complexity : O(n^2) worst/average case, O(n) best case.
    Space complexity: O(1) — sorts in place.

    Parameters
    ----------
    lst : list[int]
        The list to sort.  The original list is NOT modified.

    Returns
    -------
    list[int]
        A new list containing the same integers sorted in ascending order.
    """
    data = lst[:]          # work on a copy so the original stays unchanged
    n = len(data)

    for i in range(n - 1):
        swapped = False    # reset the flag at the start of each pass

        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True   # at least one swap occurred this pass

        # If no swap happened the list is fully sorted — stop early
        if not swapped:
            break

    return data


# ---------------------------------------------------------------------------
# Quick demonstration when the file is run directly
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import random

    sample = random.sample(range(1, 101), 10)
    print("Original list   :", sample)
    print("Basic sort      :", bubble_sort_basic(sample))
    print("Optimized sort  :", bubble_sort_optimized(sample))

    already_sorted = list(range(1, 6))
    print("\nAlready sorted  :", already_sorted)
    print("Basic sort      :", bubble_sort_basic(already_sorted))
    print("Optimized sort  :", bubble_sort_optimized(already_sorted))
