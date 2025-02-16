def quickselect_k_min(arr, k):
    """
    This function finds the k-th minimum value in a list.

    Args:
        arr: A numbers array.
        k: The k-th minimum value to find.

    Returns:
        The k-th minimum value.
    """
    if k < 1 or k > len(arr):
        return None
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    if k <= len(left):
        return quickselect_k_min(left, k)
    elif k > len(arr) - len(right):
        return quickselect_k_min(right, k - (len(arr) - len(right)))
    return pivot


if __name__ == "__main__":

    test_arrays = [
        {"arr": [3, 5, 1, 2, 7, 8, 4, 6], "k": 3},
        {"arr": [1, 2, 3, 4, -5, 6, 7, 8], "k": 5},
        {"arr": [8.3, 7, 6, 5, 4, 3, 2, 1], "k": 2},
        {"arr": [], "k": 1},
    ]

    for test in test_arrays:
        arr = test["arr"]
        k = test["k"]
        k_min = quickselect_k_min(arr, k)
        print(f"\nArray: {arr}")
        print(f"{k}-th Minimum: {k_min}")
