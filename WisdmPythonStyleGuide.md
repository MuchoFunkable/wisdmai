# Wisdm Python Style Guide 


## References 

* [Consistency](#Consistency) 
* [Pep 8](#PEP-8) 
* [Almost always use single quotes](#almost-always-use-single-quotes)
* [Line breaks and trailing commas](#line-breaks-and-trailing-commas)
* [Long function calls](#long-function-calls)

### Consistency 

The purpose of this style guide is so that the team can develop consistent code across our code base. If being consistent sacrifices the readability of our code, then we're better off being consistent. 

The style guide is meant to be collaborative across the team, so we can update it whenever a change needs to be made. 

### PEP 8


The PEP 8 Style Guide is a widely used coding convention across the standard library in the main Python distribution. In the case where something is not covered in the Wisdm Python Style Guide, the PEP 8 document should help guide styling. 

### Almost always use single line quotes 

Use single quotes unless the string itself contains single quotes. In which case, use double quotes.

Yes:
```python
error_message = 'You have done something wrong'
consolation_message = "It's okay. People make mistakes."
scientific_names['pineapple'] = 'Ananus sativus'
```

No:
```python
error_message = "You have done something wrong"
consolation_message = 'It\'s okay. People make mistakes'
scientific_names["pineapple"] = "Ananus sativus"
```

For triple-quoted strings however, always use double quotes, c/o [PEP 8 String Quotes](https://www.python.org/dev/peps/pep-0008/#string-quotes).

_Note: If double quotes is the default quote for your keyboard locale, use double quotes instead._

### Line breaks and trailing commas
Break lists, sets, and dictionaries into multiple lines. The first item should be on the next line. Add a trailing comma.

Yes:
```python
fruits = [
    'pineapple',
    'guava',
    'banana',
    'tomato',
]

scientific_names = {
    'pineapple': 'Ananus sativus',
    'guava': 'Psidium guava',
    'banana': 'Musa paradisicum',
    'tomato': 'Lycopersican esculentum',
}
```

No:
```python
fruits = ['pineapple',
          'guava',
          'banana',
          'tomato']

scientific_names = {'pineapple': 'Ananus sativus',
                    'guava': 'Psidium guava',
                    'banana': 'Musa paradisicum',
                    'tomato': 'Lycopersican esculentum'}

```

If a list does not exceed the max line length, then it could be written in one line.

OK:
```python
fruits = ['pineapple', 'guava', 'banana', 'tomato']
```

### Long function calls
Break function calls into multiple lines if they exceed the max line length. Similar to lists.

Yes:
```python
guess_fruit(
    color='red',
    size='small',
    climate='cold',
    region='north america',
    minimum_tastiness_factor=4.3,
)
```

No:
```python
guess_fruit(color='red', size='small', climate='cold',
            region='north america', minimum_tastiness_factor=4.3)
```

If the arguments do not exceed the max line length, then you may keep the arguments in one line. No trailing comma. The closing parenthesis must be on the same level as the opening parenthesis.

OK:
```python
guess_fruit(
    color='red', size='small', climate='cold', region='north america'
)
```

No:
```python
guess_fruit(
    color='red', size='small', climate='cold', region='north america')

guess_fruit(
    color='red', size='small', climate='cold', region='north america',
)  # No trailing comma
```



