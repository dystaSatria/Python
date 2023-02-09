# Lambda
#### _small anonymous function._

A lambda function can take any number of arguments, but can only have one expression.

## Syntax

```bash
lambda arguments : expression

```

## Example

```python
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun(): 
    print(value)

```
```output
1
2
3
```


### return


> Return is our way to return a value and stop all process functions that are already running.




```python 
def simpleGeneratorFun():
    yield 1
    return 2
    yield 3

for value in simpleGeneratorFun(): 
    print(value)

```
```output
1
```
