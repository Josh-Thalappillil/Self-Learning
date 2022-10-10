from typing import List
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#Example 1:
nums = [2,7,11,15] 
target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]

#Example 3:
#Input: nums = [3,3], target = 6
#Output: [0,1]

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range (len(nums)):
        for x in range (i + 1, len(nums)):
            #if we compare the first number to the second and if it equals the target we return the indices 
            if nums[x] == target - nums[i]:
                print(i, x)
                return [i, x]

def twoSumv2(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range (len(nums)):
        result = target - nums[i]
        if result in hashmap:
            print(hashmap[result], i)
            return [hashmap[result], i]
        hashmap[nums[i]] = i
        

twoSum(nums, target)
twoSumv2(nums, target)