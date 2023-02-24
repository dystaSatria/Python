# Lambda
#### _small anonymous function._

A lambda function can take any number of arguments, but can only have one expression.

## Syntax

```bash
lambda arguments : expression

```

## Example 1

```python
greeting = lambda name: print(f"Hello, {name}") 
greeting("Reza")

```

```output
Hello, Reza
```

## Example 2

```python
exam = lambda a, b : a * b
print(exam(5, 6))

```

```output
30
```

## Example 3

```python
exam = lambda a, b, c: a + b + c
print(exam(5, 6, 2))

```

```output
60
```

## Example 4

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

```

```output
22
```

## Example 5

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(12))

```

```output
48
```

## Example 6

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))


```

```output
22
33
```
