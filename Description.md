## English version

## EXERCISE
  We want to count the number of paths with at most k turns starting from the upper left cell and reaching the lower right cell in an n x n matrix.
  In the course of a walk from the generic cell (i, j) one can move to the cell at the bottom (i.e. the cell (i + i, j)) or to the cell on the right (i.e. the cell (i , j + 1)).
  A move is considered a turn if you were moving along a row and then moving along a column or vice versa.
  Design an algorithm that solves the problem in O (n2k) time.
  For example: for n = 4 and k = 2 the answer is 6

## Italian version

### ESERCIZIO 
  Vogliamo contare il numero di cammini con al più k svolte che partono dalla
  cella in alto a sinistra e raggiungono la cella in basso a destra in una matrice
  n x n.
  Nel corso di un cammino dalla generica cella (i, j) ci si può spostare nella cella
  in basso (vale a dire la cella (i + i, j)) o nella cella a destra (vale a dire la cella
  (i, j + 1)).
  Un movimento è considerato una svolta se ci si stava spostando lungo una riga
  e poi ci si sposta lungo una colonna o viceversa.
  Progettare un algoritmo che risolve il problema in tempo O(n2k).
  Ad esempio: per n =4e k = 2 la risposta è 6
