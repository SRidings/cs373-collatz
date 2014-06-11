#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % coverage3 run --branch TestCollatz.py

To obtain coverage of the test:
    % coverage3 report -m
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    
    def test_read2 (self) :
        r    = StringIO("3 2\n10 1\n50 25\n1000 250\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  3)
        self.assertEqual(j, 2)

    def test_read3 (self) :
        r    = StringIO("999999 999999\n500 1000\n20 400\n400 20\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  999999)
        self.assertEqual(j, 999999)

    def test_read4 (self) :
        r    = StringIO("1 1\n5 5\n12 13\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 1)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)
    
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
    
    def test_eval_6 (self) :
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

    def test_eval_7 (self) :
        v = collatz_eval(12, 13)
        self.assertEqual(v, 10)
    
    def test_eval_8 (self) :
        v = collatz_eval(999999, 999999)
        self.assertEqual(v, 259)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 5, 5, 6)
        self.assertEqual(w.getvalue(), "5 5 6\n")

    def test_print4 (self) :
        w = StringIO()
        collatz_print(w, 12, 13, 10)
        self.assertEqual(w.getvalue(), "12 13 10\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO("1 1\n5 5\n12 13\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n5 5 6\n12 13 10\n")

    def test_solve2 (self) :
        r = StringIO("999999 999999\n500 1000\n20 400\n400 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "999999 999999 259\n500 1000 179\n20 400 144\n400 20 144\n")

    def test_solve2 (self) :
        r = StringIO("3 2\n10 1\n50 25\n1000 250\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "3 2 8\n10 1 20\n50 25 112\n1000 250 179\n")


# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py
FFFF..F
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 47, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 51, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 55, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 59, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 78, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (failures=5)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      0      0    97%   86
----------------------------------------------------------
TOTAL            51      1      6      0    98%
"""
