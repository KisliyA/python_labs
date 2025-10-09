def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(dict.fromkeys(sorted(nums)))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))