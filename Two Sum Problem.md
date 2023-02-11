# Problem
## 1.
Input: nums = [1,4,10,-3], target = 14
Output: [1,2] or [2,1] # 4 + 10 = 14
Input: nums = [9,5,1,23], target = 10
Output: [0,2] or [2,0] # 9 + 1 = 10
Input: nums = [1,-2,5,10], target = -1
Output: [0,1] or [1,0] # 1 + -2 = -1
"""


def twoSum(self, nums: List[int], target: int) -> List[int]: #-> is not syntax in python3 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    
                    
                    
                    
 
