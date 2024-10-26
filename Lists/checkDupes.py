def contains_duplicate(nums):
    seen = set()
    for i in nums:
        if i not in seen:
            return True
        seen.add(i)
    return False
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicate(nums))