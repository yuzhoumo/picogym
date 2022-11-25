# Enhance!

- flag: picoCTF{3nh4nc3d_aab729dd}

## Problem Description

Download the image file and find the flag.

## Writeup

By opening the SVG file in a text editor, we see that the flag is hidden in
inside of the following segment:

```
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3748">p </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.08942"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3754">i </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.09383"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3756">c </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.09824"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3758">o </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.10265"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3760">C </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.10706"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3762">T </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.11147"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3764">F { 3 n h 4 n </tspan><tspan
sodipodi:role="line"
x="107.43014"
y="132.11588"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan></text>
```

At this point, we can either manually type out the flag or clean it up
automatically using some shell commands:

```bash
grep '</tspan>' drawing.flag.svg | cut -d '>' -f2 | cut -d '<' -f1 | tr -d '\n '
```

**Explanation:**

The `|` (pipe) character allows "piping" one command's output into the input
for another command. We extract the flag using the following:

1. `grep '</tspan>' drawing.flag.svg`: get all lines containing '</tspan>'

```plaintext
id="tspan3748">p </tspan><tspan
id="tspan3754">i </tspan><tspan
id="tspan3756">c </tspan><tspan
id="tspan3758">o </tspan><tspan
id="tspan3760">C </tspan><tspan
id="tspan3762">T </tspan><tspan
id="tspan3764">F { 3 n h 4 n </tspan><tspan
id="tspan3752">c 3 d _ a a b 7 2 9 d d }</tspan></text>
```

2. `cut -d '>' -f2`: remove everything to the left of '>'

```plaintext
p </tspan
i </tspan
c </tspan
o </tspan
C </tspan
T </tspan
F { 3 n h 4 n </tspan
c 3 d _ a a b 7 2 9 d d }</tspan
```

3. `cut -d '<' -f1`: remove everything to the right of '<'

```plaintext
p 
i 
c 
o 
C 
T 
F { 3 n h 4 n 
c 3 d _ a a b 7 2 9 d d }
```

4. `tr -d '\n '`: remove whitespace and newlines

```plaintext
picoCTF{3nh4nc3d_aab729dd}
```

