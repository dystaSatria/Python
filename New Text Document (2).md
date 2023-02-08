# Yield


The Yield keyword in Python is similar to a "return" statement used for returning values or objects in Python.  


## Different from 'return'

### yield

```bash

Yield is one of our ways to return a value and pause the execution of the 
currently running function.


```

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




## Example Codes

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
