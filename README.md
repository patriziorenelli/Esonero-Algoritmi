## General Description 
  This repository contains the execution of an exemption of "Algorithm Design" of the three-year degree course of the "La Sapienza University of  Rome".
## Exercise
  We want to count the number of paths with at most k turns starting from the upper left cell and reaching the lower right cell in an n x n matrix.
  In the course of a walk from the generic cell (i, j) one can move to the cell at the bottom (i.e. the cell (i + i, j)) 
  or to the cell on the right (i.e. the cell (i , j + 1)).
  A move is considered a turn if you were moving along a row and then moving along a column or vice versa.
  Design an algorithm that solves the problem in O (n2k) time.
  For example: for n = 4 and k = 2 the answer is 6
