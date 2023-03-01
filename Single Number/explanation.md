
# Single Number

Remember the ```set``` function in python. Set will be remove the duplicate.

To find the single element :
```
(2 * total the removed duplicate element) - total element 
```
So in python we can code it like :
```python
2*sum(list(set(nums))) - sum(nums)
```
