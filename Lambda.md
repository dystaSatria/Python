# Lambda
#### _A lambda function is a small anonymous function._

The Yield keyword in Python is similar to a "return" statement used for returning values or objects in Python.  


## Different from 'return'

### yield



> Yield is one of our ways to return a value and pause the execution of the 
> currently running function.


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
