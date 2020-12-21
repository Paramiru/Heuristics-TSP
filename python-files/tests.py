import math
import graph
import random
import numpy as np
import timeit

def random_euclidean(n):
    file = open("euclidean_test", "w+")
    for _ in range(n):
        file.write('{x} {y}\n'.format(x=(random.uniform(0,2000)), y=(random.uniform(0,2000))))
    file.close()

def non_metric(n):
    result = []
    for _ in range(n):
        result.append([0] * n)
    for i in range(n-1):
        # Using Gaussian distributing functions
        arr = list(np.random.normal(100,40,n-1-i))
        for j in range(i+1,n):
            e = abs(arr.pop())
            # Symmetric TSP problem
            result[i][j] = int(e)
            result[j][i] = int(e)
    file = open("non_metric", "w+")
    # Do not repeat the values twice
    hello = ""
    for i in range(n-1):
        for j in range(i+1,n):
            hello += ("{x} {y} {distance}\n".format(x=i, y=j, distance=result[i][j]))
    # This removes the empty line since for the non-Euclidean case
    # we use files which do not end in newline, like sixnodes
    hello = hello[:-1]
    file.write(hello)
    file.close()

# function to parse file from the Internet website
# (the one in references) as a file we can use 
def parse_text_file(filename):
    file = open(filename,"r")
    contents = file.read().split('\n')
    points = []
    for point in contents:
        point = point.strip()
        point = point.split(' ')
        while '' in point:
            point.remove('')
        points.append(point[1:])     
    points = points[:-2]
    print(points)
    file.close()
    file = open("new_" + filename ,"w")
    for point in points:
        file.write("{x} {y}\n".format(x=point[0],y=point[1]))
    file.close()
    
def parse_optimal_tour(filename):
    file = open(filename, "r")
    perm = []
    # optimal tour given from permutation {1, ..., N} 
    # therefore, we need to subtract 1 from each index
    for l in file.read().split('\n')[:-1]:
        perm.append(int(l) - 1)
    return perm

def time(com):
    return timeit.timeit(com, number = 1, globals = globals())
def reset_perm(graph):
    # Reset permutation to the one we had when 
    # we initialized the graph.
    graph.perm = list(range(len(graph.perm)))

def printValues(g):
    # n = -1 if is Euclidean else 1
    t = round(time("g.tourValue()"),7)
    print("Value of initial permutation:       " + str(round(g.tourValue(),2)))
    print("Time to run graph.tourValue():      " + str(t))
    reset_perm(g)
    t = round(time('g.swapHeuristic()'),7)
    print("Value of swapHeuristic:             " + str(round(g.tourValue(),2)))
    print("Time of graph.swapHeuristic():      " + str(t))
    reset_perm(g)
    t = round(time('g.TwoOptHeuristic()'),7)
    print("Value of TwoOptHeuristic:           " + str(round(g.tourValue(),2)))
    print("Time of graph.TwoOptHeuristic():    " + str(t))
    reset_perm(g)
    t = round(time('g.Greedy()'),7)
    print("Value of Greedy:                    " + str(round(g.tourValue(),2)))
    print("Time to run graph.Greedy():         " + str(t))
    reset_perm(g)
    t = round(time('g.myAlgorithm(0)'),7)
    print("Value of myAlgorithm(0):            " + str(round(g.tourValue(),2)))
    print("Time of graph.myAlgorithm(0):       " + str(t))


# Running this will print the times and cost of 
# every algorithm for cities50. These work for same 
# kind of files as long as they have an extra empty 
# line like cities25, cities50 or cities75
# Can use non-euclidean if changing -1 for n>0
# try using sixnodes or the file created by non_metric(n)
# which is called "non_metric"

filename = "cities50"
print("################ FILE --> " + filename + " ################")
print()
g = graph.Graph(-1, filename)
printValues(g)

# Create files: 

# random_euclidean(5000)
# non_metric(2000)

# Other debugging lines of code:

# g.TwoOptHeuristic()
# g.swapHeuristic()
# g.myAlgorithm(0)
# g.perm = parse_optimal_tour(filename)
# print(g.tourValue())
# print(time('g.myAlgorithm(0)'))
# print(g.tourValue()) 
# print(round(g.tourValue(),3))
# non_metric(2000)
# random_euclidean(100)