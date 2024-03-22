# Add Binary Problem

## Question 

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

```
Input: a = "11", b = "1"
Output: "100"
```

Example 2:

```
Input: a = "1010", b = "1011"
Output: "10101"
```

Constraints:

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.


## Solve

```python
main.py
```
## Explanation of the `addBinary` Function

The `addBinary` function within the `Solution` class is designed to add two binary numbers given as strings. Below are the step-by-step details of the function's operation:

## How It Works

- **Initialization**: The function starts by initializing some variables. `s` is used to store the binary sum as a list of strings, `var` is a variable to store the carry and intermediate sum, and `i`, `j` are indexes to access characters from strings `a` and `b` from back to front.

- **Iteration**: The function then iterates as long as there are digits left to process in either string (`a` or `b`) or there is a carry value (`var`). In each iteration:
  - If index `i` is valid (not negative), the binary digit from `a` at position `i` is added to `var`, and `i` is decreased to move to the next digit.
  - If index `j` is valid, the same process is applied for string `b`.
  - The result of `var % 2` (which will be `0` or `1`) is added to the list `s`. This represents the last digit of the binary sum for the current iteration.
  - The carry for the next iteration is obtained by dividing `var` by `2` using integer division (`var //= 2`).

- **Combining the Result**: Since the digits of the result are added to the list `s` from right to left, the list needs to be reversed to get the final result in the correct order. The function returns the binary sum as a string by joining the reversed `s` list.

## Example

Given `a = "1010"` and `b = "1011"`, the `addBinary` function will return `"10101"` as the binary sum of the two numbers.

This function provides an efficient solution for binary addition by leveraging basic string and arithmetic operations, without the need to convert the binary numbers to decimal format for the addition.
