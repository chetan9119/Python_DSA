nums = [2, 7, 11, 15]
target = 9

# # Brute force solution
# def twoSum(arr, target):
#     pairs = []
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             # Exculding case where (3,3) == 6
#             if arr[i] == arr[j]:
#                 continue
#             elif target - arr[i] == arr[j]:
#                 pairs.append((i,j))       
#     return pairs
# print(twoSum(nums, target))


# # Solution using dict
# def twoSum(nums, target):
#     hashMap = dict()     # OR {}
#     n = len(nums)
#     indexList = []
#     for i in range(n):
#         # checking for the required value to be mapped to
#         requiredValue = target - nums[i]
#         # if it already exists in hashmap record the indexes
#         if requiredValue in hashMap:
#             indexList.append(i)
#             indexList.append(hashMap[requiredValue])
#         # if not present, add it to the hashmap
#         else:
#             hashMap[nums[i]] = i
#         return indexList
#print(twoSum(nums, target))

# Course solution
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
print(twoSum(nums, target))