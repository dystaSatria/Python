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





# Solution

We must pay attention to the **"You may assume that each input would have exactly one solution,and you may not use the same element twice."**.That mean's we will use **Brute Force** to solve this problem. 
**Brute Force** is just calculate every single combination until you find the right answer. We can see the picture below to increase our understanding.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52683214573/in/dateposted-public/" title="Screenshot (509)"><img src="https://live.staticflickr.com/65535/52683214573_8e2f41bc1c_w.jpg" width="400" height="363" alt="Screenshot (509)"></a>
