# PW Crack 1

- flag: picoCTF{545h_r1ng1ng_1b2fd683}

## Problem Description

Can you crack the password to get the flag? Download the password checker
and you'll need the encrypted flag in the same directory too.

## Writeup

The password is hardcoded into the Python file. Opening it, we can see that
the if statement checks for the password `8713`. The flag prints after we
run the program and enter this password.

