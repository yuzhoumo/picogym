# patchme.py

- flag: 

## Problem Description

Can you get the flag? Run the Python program in the same directory as the
encrypted flag.

## Writeup

We can bypass the password check by editing the file and directly calling
`str_xor(flag_enc.decode(), "utilitarian")` before the if statement. The
return value of this function is the flag.

