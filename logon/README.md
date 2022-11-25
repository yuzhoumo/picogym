# logon

- flag: picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}

## Problem Description

The factory is hiding things from all of its users. Can you login as Joe and
find what they've been looking at?
https://jupiter.challenges.picoctf.org/problem/44573/ or
http://jupiter.challenges.picoctf.org:44573

## Writeup

The website allows us to sign in by submitting an empty username and password
(but still doesn't reveal the flag). Using the browser's debugger, we can see
there is a cookie created with an `admin` field set to `false`. The flag is
displayed when we manually set this value to `true` and refresh the page.

