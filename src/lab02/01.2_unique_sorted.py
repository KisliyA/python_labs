def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(dict.fromkeys(sorted(nums)))
print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([0,1.0,2.5]))