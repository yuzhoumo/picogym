# bloat.py

- flag: picoCTF{d30bfu5c4710n_f7w_b8062eec}

## Problem Description

Can you get the flag? Run this Python program in the same directory as this
encrypted flag.

## Writeup

`bloat.flag.py` is an obfuscated python file. WHen run, it asks for a password.

Opening the file, we see that `arg133` is the function that is called to check
the password. It returns `True` if the string passed in matches the string in
the if condition. We can force this function to always return `True` by adding
`return True` before the check (bypassing it).

After our modification, running the python file prints the flag.

