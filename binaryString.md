# Binary String

Binary String is sequence of bytes like "1" or "0"

## Example
```python
def check(bincontrol):
    a = set(bincontrol)
    b = {'0','1'}
    
    if a == b or b == "0" or b == "1" :
        print("binary string")
    else:
        print("non-binary string")

s1 = "10110010101"
check(s1)
s2 = "29389929210101"
check(s2)

```

```

```
