# List cleaner

## Instructions

Create a file `shopping.py` with a function `clean_list(shopping_list)`. 

This function input is a list of string, like this:

```python
['tomatoes', 'pastas', 'milk', 'salt']
```

For each list item, your function `clean_list` should:

* remove all spaces before and after (but not between words)
* uppercase first letter (only)
* add it index number before and a separator `'x/ '`

For example :

```python
clean_list(['tomatoes', 'pastas', 'milk', 'salt']) == ['1/ Tomatoes', '2/ Pastas', '3/ Milk', '4/ Salt']
```


## Usage

Here is a possible `test.py` to test your functions:

```python
import shopping

if __name__ == '__main__':
    shopping_list = ['tomatoes', 'pastas', 'milk', 'salt']
    print(shopping.clean_list(shopping_list))
```

```bash
$ python test.py
['1/ Tomatoes', '2/ Pastas', '3/ Milk', '4/ Salt']
```

## Notions

* [string methods](https://www.w3schools.com/python/python_ref_string.asp)
* [enumerate](https://realpython.com/python-enumerate/)
