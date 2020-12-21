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
            for line in file.read().split('\n'):
                line = line.strip()
                line = line.split(' ')
                # for e in line:
                #     if e is not " ":
                #         elements.add(e)
                while '' in line:
                    line.remove('')
                elements.add(line[0])
                elements.add(line[1])
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
        for _ in range(self.n):
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
        for _ in range(self.n):
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
        for i in range(l-1):
            # print(i, total)
            # print("Value of i:              " + str(i))
            # print("Value of self.perm[i]:   " + str(self.perm[i]))
            # print("Value of self.perm[i+1]: " + str(self.perm[i+1]))
            # print("Value of total:          " + str(total))
            # print()
            total += self.dists[self.perm[i]][self.perm[i+1]]
        # Take into account wraparound
        total += self.dists[self.perm[l-1]][self.perm[0]]
        return total

    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        if (i >= self.n):
            print ("The number tried has to be between 0 and n-1")
            return False
        if i == 0:
            j = self.perm[self.n-1]
        else:
            j = self.perm[i-1]
        k, l, m = self.perm[i], self.perm[(i+1) % self.n], self.perm[(i+2) % self.n]
        
        dist1 = self.dists[j][k] + self.dists[l][m] 
        dist2 = self.dists[j][l] + self.dists[k][m]
        if dist1 > dist2:       # In this case we swap orders
            temp = self.perm[i]
            self.perm[i] = self.perm[(i+1) % self.n]
            self.perm[(i+1) % self.n] = temp
            return True
        return False
        
    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):
        # print(i,j)
        b, e = i, j 
        # if j < i:
        #     b, e = j, i
        comp1 = self.perm[(e+1) % self.n]
        if b == 0:
            comp2 = self.perm[self.n-1]
        else:
            comp2 = self.perm[b-1]
        dist1 = self.dists[comp2][self.perm[b]] + self.dists[self.perm[e]][comp1]
        dist2 = self.dists[comp2][self.perm[e]] + self.dists[self.perm[b]][comp1]
        if dist1 > dist2:
            to_reverse = self.perm[i:j+1]
            to_reverse.reverse()
            self.perm[i:j+1] = to_reverse
            return True
        return False

    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
                

    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        permutation = []
        permutation.append(self.perm[0])
        copy = self.perm.copy()
        copy.remove(self.perm[0])
        while (len(permutation) != len(self.perm)):
            minimum = float("inf")
            dict = {}  
            for i in copy:
                # if i != permutation[-1]:
                k = self.dists[i][permutation[-1]]
                # if edges with same distance just consider the first one!
                if k not in dict.keys():   
                    dict[k] = i
                if k < minimum and k > 0:
                    minimum = k
            copy.remove(dict[minimum])
            permutation.append(dict[minimum])
        self.perm = permutation
        
    def minimum_edge(self, key, isInMST):
        minimum = float("inf")
        for vertex in range(self.n):
            if not isInMST[vertex] and key[vertex] < minimum:
                minimum = key[vertex]
                vertex_to_return = vertex
        return vertex_to_return

    def MST_Prim(self, matrix, root):
        isInMST = [False] * self.n 
        parent = [None] * self.n
        key = [float("inf")] * self.n
        key[root] = 0          # This way we select our root
        parent[root] = -1      # Root has no parent
        
        # Update values of adjacent nodes!
        # Only if not in MST. Keep a record of already chosen nodes
        # There is an adjacent node if self.dists[u][v] > 0
        for _ in range(self.n):
            # Choose minimum vertex starting with our root
            u = self.minimum_edge(key, isInMST)
            # Value added to MST
            isInMST[u] = True 
            for v in range(self.n):
                if matrix[u][v] > 0 and matrix[u][v] < key[v] and not isInMST[v]:
                    key[v] = matrix[u][v]
                    parent[v] = u
        return parent

    def build_Tree_recursion(self, dict, node):
         if dict[node.value] != []:
            node.children = dict[node.value]
            for child in node.children:
                child.children = dict[child.value]
                self.build_Tree_recursion(dict, child)
    
    def build_Tree(self, parent, root):
        # first we get a dictionary mapping parent and all children
        parent_children = defaultdict(list)
        # Use lists so that we can append the nodes as instances
        # of our class TreeNode()
        for child in range(self.n):
            parent_children[parent[child]].append(TreeNode(child))
        tree_root = TreeNode(root)
        # Once we have the root and the "family" as a dictionary
        # we can build the tree
        self.build_Tree_recursion(parent_children, tree_root)
        return tree_root
    
    def DFS(self, node, visited, permutation):
        # Code to traverse the n-ary tree 
        visited[node.value] = True
        permutation.append(node.value)
        for child in node.children:
            # Do not repeat nodes which have been visited
            if visited[child.value] == False:
                self.DFS(child, visited, permutation)

    def myAlgorithm(self, root):
        parent = self.MST_Prim(self.dists, root)
        tree_root = self.build_Tree(parent, root)
        visited = [False] * self.n
        permutation = []
        self.DFS(tree_root, visited, permutation)
        self.perm = permutation
        # Run DFS on tree_root to get the final permutation
        # Taking into account which node has been visited