# fixme2.py

- flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b} 

## Problem Description

Fix the syntax error in the Python script to print the flag.

## Writeup

There is a missing `=` in the if statement. `if flag = "":` should instead be
`if flag == "":`. In Python, `=` denotes assignment while `==` denotes
comparison of equality.

