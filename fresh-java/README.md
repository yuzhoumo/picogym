# Fresh Java

- flag: picoCTF{700l1ng_r3qu1r3d_738cac89}

## Problem Description

Can you get the flag? Reverse engineer this Java program.

## Writeup

We're given a Java class file, which needs to first be decompiled.
Decompiling this file yields the following:

```java
import java.util.Scanner;

// 
// Decompiled by Procyon v0.5.36
// 

public class KeygenMe
{
  public static void main(final String[] array) {
    final Scanner scanner = new Scanner(System.in);
    System.out.println("Enter key:");
    final String nextLine = scanner.nextLine();
    if (nextLine.length() != 34) {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(33) != '}') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(32) != '9') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(31) != '8') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(30) != 'c') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(29) != 'a') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(28) != 'c') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(27) != '8') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(26) != '3') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(25) != '7') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(24) != '_') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(23) != 'd') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(22) != '3') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(21) != 'r') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(20) != '1') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(19) != 'u') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(18) != 'q') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(17) != '3') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(16) != 'r') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(15) != '_') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(14) != 'g') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(13) != 'n') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(12) != '1') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(11) != 'l') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(10) != '0') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(9) != '0') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(8) != '7') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(7) != '{') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(6) != 'F') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(5) != 'T') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(4) != 'C') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(3) != 'o') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(2) != 'c') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(1) != 'i') {
      System.out.println("Invalid key");
      return;
    }
    if (nextLine.charAt(0) != 'p') {
      System.out.println("Invalid key");
      return;
    }
    System.out.println("Valid key");
  }
}
```

At this point, we can either manually type in the flag or use some shell
commands to clean this up automatically:

```bash
grep "'" decompiled.java | cut -d "'" -f2 | tr -d '\n' | rev
```

**Explanation:**

The `|` (pipe) character allows "piping" one command's output into the input
for another command. We extract the flag using the following:

1. `grep "'" decompiled.java`: get all lines containing `'`

```plaintext
if (nextLine.charAt(33) != '}') {
if (nextLine.charAt(32) != '9') {
if (nextLine.charAt(31) != '8') {
if (nextLine.charAt(30) != 'c') {
if (nextLine.charAt(29) != 'a') {
if (nextLine.charAt(28) != 'c') {
if (nextLine.charAt(27) != '8') {
if (nextLine.charAt(26) != '3') {
if (nextLine.charAt(25) != '7') {
if (nextLine.charAt(24) != '_') {
if (nextLine.charAt(23) != 'd') {
if (nextLine.charAt(22) != '3') {
if (nextLine.charAt(21) != 'r') {
if (nextLine.charAt(20) != '1') {
if (nextLine.charAt(19) != 'u') {
if (nextLine.charAt(18) != 'q') {
if (nextLine.charAt(17) != '3') {
if (nextLine.charAt(16) != 'r') {
if (nextLine.charAt(15) != '_') {
if (nextLine.charAt(14) != 'g') {
if (nextLine.charAt(13) != 'n') {
if (nextLine.charAt(12) != '1') {
if (nextLine.charAt(11) != 'l') {
if (nextLine.charAt(10) != '0') {
if (nextLine.charAt(9) != '0') {
if (nextLine.charAt(8) != '7') {
if (nextLine.charAt(7) != '{') {
if (nextLine.charAt(6) != 'F') {
if (nextLine.charAt(5) != 'T') {
if (nextLine.charAt(4) != 'C') {
if (nextLine.charAt(3) != 'o') {
if (nextLine.charAt(2) != 'c') {
if (nextLine.charAt(1) != 'i') {
if (nextLine.charAt(0) != 'p') {
```

2. `cut -d "'" -f2`: remove everything outside of `'`

```plaintext
}
9
8
c
a
c
8
3
7
_
d
3
r
1
u
q
3
r
_
g
n
1
l
0
0
7
{
F
T
C
o
c
i
p

```

3. `tr -d '\n'`: remove newlines

```plaintext
}98cac837_d3r1uq3r_gn1l007{FTCocip
```

4. `rev`: reverse the string

```plaintext
picoCTF{700l1ng_r3qu1r3d_738cac89}
```

