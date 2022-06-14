# Raise an exception

## Instruction

Create a file `recipes.py` with a function `create_recipe` that take 3 parameters:

* name: the recipe name as string
* persons: number of persons as integer
* ingredients: list of ingredients (list of strings)

This function check if recipe data are correct and simply return a dictionary.

```python
{
    'title': '...', 
    'persons': ..., 
    'ingredients': [...],
}
```

The function should raise a `ValueError` with specific message in those cases:

* if `title` has more than 150 character length. Error message: `"Title is tool long"`
* if `persons` is null or greater than 50. Error message: `"Invalid person number"`
* if `ingredients` list is empty. Error message: `"This recipe has no ingredients"`

## Usage

Here is a possible `test.py` to test your functions:

```python
import recipes

if __name__ == '__main__':
    print(recipes.create_recipe('Pâtes au beurre', 30, ['pâtes', 'beurre']))
```

```bash
$ python test.py
{'title': 'Pâtes au beurre', 'persons': 30, 'ingredients': ['pâtes', 'beurre']}
```

## Notions

* [built-in exceptions](https://www.w3schools.com/python/python_ref_exceptions.asp)
