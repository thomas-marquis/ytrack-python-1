# String tokenizer

## Instructions

Tokenization is the process of separating words from a sentence. It often the first step in text analysis.
Here, we implement or own string tokenizer.

Create a file `string_processing.py` with a function `tokenize(sentence)`.

Given a sentence, this function should :

* separate each word ("n'est" => 2 words, "c'est-à-dire" => 4 words)
* put words to lower case
* remove all punctuation sign and special character. Given token must be only letters or numbers

## Usage

Here is a possible `test.py` to test your functions:

```python
import string_processing

if __name__ == '__main__':
    my_sentence = "Dites, on n'attend pas votre soeur ?"
    print(string_processing.tokenize(my_sentence))
```

```bash
$ python test.py
['dites', 'on', 'n', 'attend', 'pas', 'votre', 'soeur']
```

## Notions

* [string methods](https://www.w3schools.com/python/python_ref_string.asp)
* [Tokenization in text analysis](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization)
* [Word segmentation](https://en.wikipedia.org/wiki/Text_segmentation#Word_segmentation)
