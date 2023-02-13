# Two Sum Problem

Given an array of integers ```nums``` and an integer ```target```, return indices of the two numbers such that they add up to ```target```.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Example 1

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Example 2

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
                     
## Example 3

```
Input: nums = [3,3], target = 6
Output: [0,1]
```





# Solution 1 (Brute Force)

- We must pay attention to the **"You may assume that each input would have exactly one solution,and you may not use the same element twice."**.That mean's we will use **Brute Force** to solve this problem. 
**Brute Force** is just calculate every single combination until you find the right answer. We can see the picture below to increase our understanding.
<p align="center">
 <img src="https://live.staticflickr.com/65535/52683214573_8e2f41bc1c_w.jpg" width="400" height="363" alt="Screenshot (509)">
</p>
<br>
<br>
<br>
<br>
### The Solved Code
```python
class Solution(object):
    def twoSum(self, nums, target): 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

# Solution 1 (Brute Force)
- After that we can use **Hash table** (dictionary / ```{}```) to collect and store the elements in the array and their indices, and then checks each element and its index whether the target minus the current element is in the hash table.

  ```python
  class Solution(object):
    def twoSum(self, nums, target):
        hashtable= {}
  ```

- We use a loop to iterate over all elements in the array(nums array's elements). So, we will use ```for in in range(len(nums)):```

  ```python
  class Solution(object):
    def twoSum(self, nums, target):
        hashtable= {}
        for in in range(len(nums)):
  ```
  
  
  
  
  
  
  
  
  
  
  
  
  
