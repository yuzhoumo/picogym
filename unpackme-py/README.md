# unpackme.py

- flag: picoCTF{175_chr157m45_5274ff21}

## Problem Description

Can you get the flag? Reverse engineer this python program.

## Writeup

The program is stored as an encrypted string, which is then decoded and
passed into exec. Printing out the decoded string yields the following:

```python
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_5274ff21}')
else:
  print('That password is incorrect.')
```

At this point, we've revealed the flag for this challenge.

