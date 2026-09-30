def min_max(nums: list[float | int]):
    if len(nums) == 0:
        raise ValueError
    lo = nums[0]
    hi = nums[0]
    for i in range(1, len(nums)):
        x = nums[i]
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi