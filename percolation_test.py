import percolation
import time
import random
import sys


def print_grid(grid):
    for row in grid:
        print(row)
    print('\n')

def visualize(n):
    perc = percolation.Percolation(n)
    print_grid(perc.grid)
    opens = 0
    while(not perc.percolates()):
        i, j = random.randint(0,n-1), random.randint(0,n-1)
        if not perc.is_open(i,j):  
            perc.open(i,j)
            opens += 1
            time.sleep(.5)
            print_grid(perc.grid)
    print_grid(perc.grid)
    print("percolation threshold =", opens/(n*n))

def montecarlo(N, T):
    perc_thresholds = []
    for t in range(T):
        perc = percolation.Percolation(N)
        opens = 0
        while(not perc.percolates()):
            i, j = random.randint(0,N-1), random.randint(0,N-1)
            if not perc.is_open(i,j):  
                perc.open(i,j)
                opens += 1
        perc_threshold = opens/(N*N)
        perc_thresholds.append(perc_threshold)
    mean_perc_threshold = sum(perc_thresholds)/len(perc_thresholds)
    print("Mean percolation threshold: ", mean_perc_threshold)

if sys.argv[1].lower() == "visualize":
    visualize(int(sys.argv[2]))
if sys.argv[1].lower() == "montecarlo":
    montecarlo(int(sys.argv[2]), int(sys.argv[3]))
