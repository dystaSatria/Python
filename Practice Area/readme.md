# String Operations in Pytho

### 1. Creating Strings
In Python, strings can be created using single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`).

```python
string_one = 'This is a string with single quotes.'
string_two = "This is a string with double quotes."
string_three = '''This is a string
that spans multiple
lines using triple quotes.'''
```

### 2. Accessing Characters in a String
Characters within a string can be accessed using indexing, which starts at 0 for the first character.

```python
s = "Hello World"
print(s[0])  # Output: H
print(s[6])  # Output: W
```

### 3. String Slicing
Slicing is used to obtain a substring from a string.

```python
s = "Hello World"
print(s[1:5])  # Output: ello
print(s[6:])   # Output: World
```

### 4. Concatenating Strings
Two or more strings can be concatenated using the `+` operator.

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  # Output: Hello World
```

### 5. String Formatting
Python offers various ways to format strings.

#### f-strings (Python 3.6+)
```python
name = "John"
age = 30
print(f"Hello, {name}. You are {age}.")  # Output: Hello, John. You are 30.
```

#### `format` method
```python
name = "John"
age = 30
print("Hello, {}. You are {}.".format(name, age))  # Output: Hello, John. You are 30.
```

### 6. String Methods
Python has a set of built-in methods that can be used to manipulate strings.

```python
s = "Hello world"

print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world
print(s.capitalize())  # Output: Hello world
print(s.title())  # Output: Hello World
print(s.replace("world", "Python"))  # Output: Hello Python
```

These basic examples and methods provided for string operations in Python illustrate how flexible and powerful the language is for string manipulation. Python offers a vast array of methods and techniques for working with strings.
