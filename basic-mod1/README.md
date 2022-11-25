# basic-mod1

- flag: picoCTF{R0UND_N_R0UND_79C18FB3}

## Problem Description

We found this weird message being passed around on the servers, we think we
have a working decryption scheme. Take each number mod 37 and map it to the
following character set: 0-25 is the alphabet (uppercase), 26-35 are the
decimal digits, and 36 is an underscore. Wrap your decrypted message in the
picoCTF flag format (i.e. picoCTF{decrypted_message}).

## Writeup

The message is a text file of space delimited integers. We can read this into
a Python script and follow the instructions to decode it:

```python
def decode(message):
  res = []
  for n in message:
    n %= 37
    if n == 36:
      res.append('_')
    elif (n>=26) and (n<=35):
      res.append(str(n-26))
    else:
      res.append(chr(ord('A') + n))

  return ''.join(res)


with open('message.txt', 'r') as f:
  message = [int(w) for w in f.read().strip().split()]
  print('picoCTF{'+decode(message)+'}')
```

