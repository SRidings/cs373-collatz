#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

numCycles = [0] * 1000000

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    global numCycles

    max = -1

    if (i > j) :

     oldI = i
     oldJ = j
     j = oldI
     i = oldJ

    if (j > i) and (i <= (j // 2)) :

     i = (j // 2)

    for num in range (i, (j+1)) :
     n = num
     assert (n > 0)           
     c = 1
       
     while (n > 1) :

      if ((n < 1000000) and (numCycles[n] != 0)) :
       c += (numCycles[n] - 1)
       break

      if (n % 2) == 0 :

       n = (n // 2)
       c += 1

      else :

       n = (((3 * n) + 1) // 2)
       c += 2
      
     assert c > 0

     if (numCycles[num] == 0) :
      numCycles[num] = c

     if (c > max) :
      max = c

    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

"""
To run the program
    % coverage3 run --branch RunCollatz.py < RunCollatz.in

To obtain coverage of the run:
    % coverage3 report -m

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys
# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

"""
% coverage3 run --branch RunCollatz.py < RunCollatz.in > RunCollatz.out



% coverage3 report -m
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz         18      0      6      0   100%
RunCollatz       5      0      0      0   100%
---------------------------------------------------------
TOTAL           23      0      6      0   100%
"""

