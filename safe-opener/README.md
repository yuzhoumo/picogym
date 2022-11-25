# Safe Opener

- flag: picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}

## Problem Description

I forgot the key to my safe but this program is supposed to help me with
retrieving the lost key. Can you help me unlock my safe? Put the password you
recover into the picoCTF flag format like: picoCTF{password}

## Writeup

The key is hardcoded in the file as `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`.
Decoding this key from base64 yields `pl3as3_l3t_m3_1nt0_th3_saf3`, which is
the flag for this problem.

