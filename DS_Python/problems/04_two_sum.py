# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    #print('[{0},{1}]'.format(i,j))
                    return [i,j]

    def twoSum2(self, nums, target):
        hash = {}
        for i in range(0, len(nums)):
            hash[nums[i]] = i

        print(hash)

        for j in range(0, len(nums)):
            complement = target - nums[j]
            if complement in hash and hash[complement] != j:
                return [j, hash[complement]]

    def twoSum2(self, nums, target):
        if len(nums) < 1:
            return False
        hash = {}
        for i in range(len(nums)):
            #if i <= target:
                complement = target - nums[i]
                if complement in hash:
                    return [hash[complement], i]
                hash[nums[i]] = i

obj = Solution()
print(obj.twoSum2([2,7,11,15], 9))
