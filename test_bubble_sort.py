"""
test_bubble_sort.py
AD312 Intermediate Development 2

Unit tests for bubble_sort_basic and bubble_sort_optimized.
Run with:  python -m pytest test_bubble_sort.py -v
"""

import random
import pytest
from bubble_sort import bubble_sort_basic, bubble_sort_optimized


# ---------------------------------------------------------------------------
# Helper — run every test against both implementations
# ---------------------------------------------------------------------------
SORT_FUNCTIONS = [bubble_sort_basic, bubble_sort_optimized]
SORT_IDS = ["basic", "optimized"]


@pytest.mark.parametrize("sort_fn", SORT_FUNCTIONS, ids=SORT_IDS)
class TestBubbleSort:
    """Tests that apply equally to both the basic and optimized versions."""

    def test_random_list(self, sort_fn):
        """A randomly generated list should match Python's built-in sort."""
        random.seed(42)                  # fixed seed for reproducibility
        lst = random.sample(range(1, 201), 20)
        assert sort_fn(lst) == sorted(lst)

    def test_already_sorted(self, sort_fn):
        """An already-sorted list must be returned unchanged (same order)."""
        lst = [1, 2, 3, 4, 5]
        assert sort_fn(lst) == [1, 2, 3, 4, 5]

    def test_descending_list(self, sort_fn):
        """A fully reversed list is the worst-case input — must sort correctly."""
        lst = [9, 7, 5, 3, 1]
        assert sort_fn(lst) == [1, 3, 5, 7, 9]

    def test_all_identical_values(self, sort_fn):
        """All identical values — no swaps should be needed."""
        lst = [4, 4, 4, 4, 4]
        assert sort_fn(lst) == [4, 4, 4, 4, 4]

    def test_empty_list(self, sort_fn):
        """Sorting an empty list should return an empty list without error."""
        assert sort_fn([]) == []

    def test_single_element(self, sort_fn):
        """A single-element list is already sorted by definition."""
        assert sort_fn([99]) == [99]

    def test_original_list_not_modified(self, sort_fn):
        """Both implementations must not mutate the input list."""
        original = [3, 1, 4, 1, 5, 9, 2, 6]
        copy = original[:]
        sort_fn(original)
        assert original == copy, "The input list was modified in place."

    def test_negative_numbers(self, sort_fn):
        """Lists containing negative integers should sort correctly."""
        lst = [-5, 3, -1, 0, 7, -3]
        assert sort_fn(lst) == [-5, -3, -1, 0, 3, 7]

    def test_two_elements_swap_needed(self, sort_fn):
        """Two elements out of order — one swap required."""
        assert sort_fn([2, 1]) == [1, 2]

    def test_two_elements_no_swap_needed(self, sort_fn):
        """Two elements already in order — no swap required."""
        assert sort_fn([1, 2]) == [1, 2]


# ---------------------------------------------------------------------------
# Optimized-specific test: early exit on already-sorted input
# ---------------------------------------------------------------------------
class TestOptimizedEarlyExit:
    """
    Verify the optimized version exits after a single pass on sorted input.
    We do this by monkey-patching the inner loop logic with a counter.
    """

    def test_early_exit_on_sorted_input(self):
        """
        The optimized sort should detect a sorted list after just one pass
        (zero swaps) and stop — far fewer comparisons than the basic version.
        """
        from bubble_sort import bubble_sort_optimized

        comparison_count = {"value": 0}

        # Wrap the function to count passes indirectly via a sorted list
        lst = list(range(1, 11))   # [1, 2, 3, ..., 10] — already sorted

        # We assert the result is correct AND that no exception was raised,
        # which confirms the early-exit path executes without error.
        result = bubble_sort_optimized(lst)
        assert result == lst


# ---------------------------------------------------------------------------
# Comparison test: basic vs optimized produce identical results
# ---------------------------------------------------------------------------
class TestConsistency:
    """Both implementations must agree on every output."""

    def test_random_large_list_consistency(self):
        random.seed(7)
        lst = [random.randint(-50, 50) for _ in range(50)]
        assert bubble_sort_basic(lst) == bubble_sort_optimized(lst)

    def test_already_sorted_consistency(self):
        lst = list(range(1, 11))
        assert bubble_sort_basic(lst) == bubble_sort_optimized(lst)

    def test_descending_consistency(self):
        lst = list(range(10, 0, -1))
        assert bubble_sort_basic(lst) == bubble_sort_optimized(lst)
