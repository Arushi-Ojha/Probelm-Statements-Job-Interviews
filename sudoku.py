import numpy as np

def sudoku():
    g=0
    a= np.array[9][9]
    for i in range (9):
        for j in range (9):
            a[i][j]=int(input("Enter a[",i,"][",j,"] element: "))
    for i in range (9):
        for j in range (9):
            if a[i][j]==0:
                g= fill[i][j]
                for k in range(9):
                    if g!=a[i]:
                        a[i][j]=g
                    
def fill(i,j):
    for q in range (9):
     return q