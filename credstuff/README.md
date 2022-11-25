# credstuff

- flag: picoCTF{C7r1F_54V35_71M3}

## Problem Description

We found a leak of a blackmarket website's login credentials. Can you find the
password of the user cultiris and successfully decrypt it? Download the leak
here. The first user in usernames.txt corresponds to the first password in
passwords.txt. The second user corresponds to the second password, and so on.

## Writeup

Using `grep -n cultiris usernames.txt`, we find that the username `cultiris`
is on line 378. Then `head -378 passwords.txt` prints out the first 378 lines
of `passwords.txt`. The last line is the password for `cultiris`, which is
encoded as `cvpbPGS{P7e1S_54I35_71Z3}`.

This looks like a substitution cipher since we see that it matches the format
of the picoCTF flag but with different letters. Trying ROT13 (Caesar cipher
with offset of 13), we get our decoded flag: `picoCTF{C7r1F_54V35_71M3}`.

