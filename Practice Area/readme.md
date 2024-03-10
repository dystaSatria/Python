# String Operations in Python

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

# Metode #1 

Metode dalam Python adalah fungsi yang terkait dengan objek, yang memungkinkan Anda untuk melakukan operasi dengan objek tersebut atau mengubah objek itu sendiri. Berikut adalah 10 contoh metode pada objek yang berbeda dalam Python, termasuk string, list, dictionary, dan lebih lanjut, lengkap dengan penjelasan singkat dan contoh penggunaan:

### 1. `append()` untuk List
Menambahkan sebuah item ke akhir list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```

### 2. `pop()` untuk List
Menghapus item pada posisi tertentu dalam list dan mengembalikannya. Jika indeks tidak ditentukan, `pop()` menghapus dan mengembalikan item terakhir dalam list.

```python
my_list = ['a', 'b', 'c', 'd']
item = my_list.pop(2)
print(item)  # Output: 'c'
print(my_list)  # Output: ['a', 'b', 'd']
```

### 3. `find()` untuk String
Mencari substring dalam string dan mengembalikan indeks awal substring tersebut. Jika tidak ditemukan, mengembalikan -1.

```python
my_string = "hello world"
index = my_string.find("world")
print(index)  # Output: 6
```

### 4. `upper()` untuk String
Mengubah semua huruf dalam string menjadi huruf besar.

```python
my_string = "hello world"
print(my_string.upper())  # Output: "HELLO WORLD"
```

### 5. `lower()` untuk String
Mengubah semua huruf dalam string menjadi huruf kecil.

```python
my_string = "HELLO WORLD"
print(my_string.lower())  # Output: "hello world"
```

### 6. `sort()` untuk List
Mengurutkan item dalam list di tempat.

```python
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]
```

### 7. `update()` untuk Dictionary
Menambahkan pasangan kunci-nilai ke dalam dictionary. Jika kunci sudah ada, nilai akan diperbarui.

```python
my_dict = {'name': 'John', 'age': 25}
my_dict.update({'age': 26, 'city': 'New York'})
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York'}
```

### 8. `remove()` untuk List
Menghapus item pertama dari list yang nilainya sama dengan parameter yang diberikan.

```python
my_list = ['a', 'b', 'c', 'd', 'b']
my_list.remove('b')
print(my_list)  # Output: ['a', 'c', 'd', 'b']
```

### 9. `strip()` untuk String
Menghapus whitespace di awal dan akhir string.

```python
my_string = "   hello world   "
print(my_string.strip())  # Output: "hello world"
```

### 10. `get()` untuk Dictionary
Mengembalikan nilai dari kunci yang ditentukan. Jika kunci tidak ditemukan, mengembalikan nilai default jika ditentukan, atau `None` jika tidak.

```python
my_dict = {'name': 'John', 'age': 25}
print(my_dict.get('age'))  # Output: 25
print(my_dict.get('city', 'Not Found'))  # Output: "Not Found"
```

# Python Lists Overview

Python lists are versatile, ordered collections of items that can be modified. They can contain elements of different types, including other lists, allowing for the construction of complex data structures. Below is a concise guide on using Python lists effectively.

## Creating Lists

To create a list, place its elements within square brackets `[]`, separated by commas.

```python
primes = [2, 3, 5, 7, 11]
empty_list = []
```

## Adding Lists Together

Use the `+` operator to concatenate lists.

```python
items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)  # ['cake', 'cookie', 'bread', 'biscuit', 'tart']
```

## List Methods

### .append()

Add an item to the end of a list.

```python
orders = ['daisies', 'periwinkle']
orders.append('tulips')
print(orders)  # ['daisies', 'periwinkle', 'tulips']
```

### .remove()

Remove the first occurrence of an item.

```python
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
shopping_line.remove("Chris")
print(shopping_line)  # ["Cole", "Kip", "Sylvana", "Chris"]
```

### .count()

Count the occurrences of an item.

```python
backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
print(backpack.count('pen'))  # 3
```

### .sort()

Sort the list in ascending order.

```python
exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)  # [1, 2, 3, 4]
```

### .insert()

Insert an item at a specific index.

```python
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line)  # ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
```

### .pop()

Remove and return an item at a given index.

```python
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop()
print(removed_element)  # 'Clowns 101'
```

## Accessing Elements

Access list elements by their index. Python uses zero-indexing.

```python
names = ['Roger', 'Rafael', 'Andy', 'Novak']
print(names[2])  # 'Andy'
```

### Negative Indices

Negative indices can be used to access elements from the end of the list.

```python
soups = ['minestrone', 'lentil', 'pho', 'laksa']
print(soups[-1])  # 'laksa'
```

## Slicing Lists

Extract sub-lists using slice notation.

```python
tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3]
print(tools_slice)  # ['hammer', 'lever']
```

## Length of a List

Use `len()` to find how many items a list has.

```python
knapsack = [2, 4, 3, 7, 10]
print(len(knapsack))  # 5
```

## Sorting Lists

Use `sorted()` to return a new list that is sorted.

```python
unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList)
print(sortedList)  # [1, 2, 3, 4]
```
