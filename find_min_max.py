""" 
This module contains a function that finds the minimum and maximum values in a list.
 """


def find_min_max(arr: list) -> tuple:
    """
    This function finds the minimum and maximum values in a list.

    Args:
        arr: A numbers array .

    Returns:
        A tuple containing the minimum and maximum values.
    """
    if len(arr) == 1:
        return arr[0], arr[0]
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    return min(left_min, right_min), max(left_max, right_max)


if __name__ == "__main__":

    test_arrays = [
        [3, 5, 1, 2, 7, 8, 4, 6],
        [1, 2, 3, 4, -5, 6, 7, 8],
        [8.3, 7, 6, 5, 4, 3, 2, 1],
    ]

    for arr in test_arrays:
        min_val, max_val = find_min_max(arr)
        print(f"\nArray: {arr}")
        print(f"Minimum: {min_val}, Maximum: {max_val}")
