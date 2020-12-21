import math
from collections import defaultdict

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)

class TreeNode:
    def __init__(self, value, c=[]):
        self.value = value
        self.children = c
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        file = open(filename, 'r')
        if n == -1:
            number_of_lines = 0
            for _ in file:
                number_of_lines += 1
            self.n = number_of_lines
            self.dists, self.input_points = self.Euclidean_dist(filename)
        if n > 0:
            elements = set()
            contents = file.read()
            contents = contents.replace('\n', ' ')
            contents = contents.replace(' ', '')
            count = 1
            for n in contents:
                if count % 3 != 0:
                    elements.add(n)
                count += 1
            self.n = len(elements)
            self.dists = self.TSP_dist(filename)
        self.perm = list(range(self.n))
    def Euclidean_dist(self,filename):
        file = open(filename, 'r')
        contents = file.read().split('\n')
        input_points = []
        points = []
        for point in contents:
            point = point.strip()
            point = point.split(' ')
            while '' in point:
                point.remove('')
            points.append(point)     
        points = points[:-1]

        # Initialize list of lists containing 
        # distances between cities
        result = []
        for i in range(self.n):
            result.append([0] * self.n) 

        point_1, point_2, counter = 0, 1, 1
        for point in points:
            pt1 = (float(point[0]), float(point[1]))
            input_points.append(pt1)
            for point2 in points[counter:]:
                pt2 = (float(point2[0]),float(point2[1]))
                dist = euclid(pt1,pt2)
                result[point_1][point_2] = dist
                result[point_2][point_1] = dist
                point_2 += 1
            counter += 1
            point_1 += 1
            point_2 = point_1 + 1
            if point_1 == self.n: 
                break 
        return result, input_points
 
    def TSP_dist(self, filename):
        nodes = []
        file = open(filename, 'r')
        for line in file.read().split('\n'):
            line = line.strip()
            line = line.split(' ')
            while '' in line:
                line.remove('')
            nodes.append(line)

        result = []
        for i in range(self.n):
            result.append([0]*self.n)
        for l in nodes:
            result[int(l[0])][int(l[1])] = int(l[2])
            result[int(l[1])][int(l[0])] = int(l[2])
        return result

    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        total = 0
        l = len(self.perm)
        for i in range(l - 1):
            # print("Value of i:              " + str(i))
            # print("Value of self.perm[i]:   " + str(self.perm[i]))
            # print("Value of self.perm[i+1]: " + str(self.perm[i+1]))
            # print("Value of total:          " + str(total))
            # print()
            total += self.dists[self.perm[i]][self.perm[i+1]]
        # Take into account wraparound
        total += self.dists[self.perm[l-1]][self.perm[0]]
        return total


# file = open("ch150", "r")
# f = open("new_ch150", "w")
# for l in file.read().split('\n')[:-1]:
#     line = l.split(' ')
#     f.write(line[1] + " " + line[2] +'\n')
#     print(line)
    
# file.close()

g = Graph(-1, "new_gr202.txt")
# g.perm = perm
print(g.tourValue())
print(g.tourValue())
#
# print(g.tourValue())
