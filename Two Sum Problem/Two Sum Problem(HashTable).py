class Solution(object):
    def twoSum(self, nums, target):
        hashtable= {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target-nums[i]],i]
            hashtable[nums[i]] = i # Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")