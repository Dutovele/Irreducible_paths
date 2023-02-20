from collections import defaultdict
import numpy as np

num_vertices = 0
num_edges = 0
total_paths = 0

class Graph:

    def __init__(self):
        self.V = num_vertices
        self.graph = defaultdict(list)
        self.edges = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.edges.append([u, v])



def create_graph():
    global num_vertices
    global num_edges

    num_vertices, num_edges = input().split(" ")
    num_vertices = int(num_vertices)
    num_edges = int(num_edges)
    # print("Num vertices",num_vertices,"Num edges", num_edges)
    g.V = num_vertices

    for temp in range(num_edges):
        temp = input().strip("\n")
        v1, v2 = temp.split(" ")
        v1 = int(v1)
        v2 = int(v2)
        g.addEdge(v1, v2)
        g.addEdge(v2, v1)


def make_neib_matrix(g):
    edges = np.array(g.edges)
    neib_matrix = np.zeros((num_vertices, num_vertices), dtype=int)
    neib_matrix[edges[:,0], edges[:,1]] = 1
    # print("Adjacency matrix for neighbours")
    # print_matrix(neib_matrix)
    return neib_matrix


def count_irreducible(g,neib_matrix):
    global total_paths

    for edg in g.edges:
        if edg[0] < edg[1]:
            for s_neib in g.graph[edg[0]]:
                if s_neib != edg[1]:
                    for e_neib in g.graph[edg[1]]:
                        if e_neib != edg[0]:
                            if s_neib != e_neib:
                                if check_irreducible(s_neib,edg,e_neib,neib_matrix):
                                    # print(s_neib, edg, e_neib)
                                    total_paths += 1
    print(total_paths)


def check_irreducible(s_neib, edge, e_neib, neib_matrix):

    if neib_matrix[s_neib][edge[1]] == 0:
        if neib_matrix[s_neib][e_neib] == 0:
            if neib_matrix[edge[0]][e_neib] == 0:
                if neib_matrix[e_neib][s_neib] == 0:
                    return True


g = Graph()
create_graph()
# print("Graph edges list", g.edges)
neib_matrix = make_neib_matrix(g)
count_irreducible(g,neib_matrix)


