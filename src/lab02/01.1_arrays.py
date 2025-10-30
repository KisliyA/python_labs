def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    maxi = max(nums)
    mini = min(nums)
    return mini,maxi
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print('ValueError')
print(min_max([1.5,2,2.0,-3.1]))
