class Solution(object):
    def twoSum(self, nums, target):
        hashtable= {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target-nums[i]],i]
            hashtable[nums[i]] = i 
