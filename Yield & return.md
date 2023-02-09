# Yield


The Yield keyword in Python is similar to a "return" statement used for returning values or objects in Python.  


## Different from 'return'

### yield

```bash

> Yield is one of our ways to return a value and pause the execution of the 
> currently running function.


```
> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

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
```bash

Return is our way to return a value and stop all process functions that are already running.


```

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
