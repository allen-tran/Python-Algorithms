import collections
from typing import Deque


class Graph:
    visited = [False] * (13)

    vertices = None

    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = [None] * (vertices)
        i = 0
        while i < vertices:
            self.adjList[i] = Deque()
            i += 1

    def addEgde(self, source, destination):
        self.adjList[source].append(destination)

    def printGraph(self):
        i = 0
        while i < self.vertices:
            if len(self.adjList[i] > 0):
                print("Vertex " + str(i) + " is connected to: ")
                j = 0
                while j < len(self.adjList[i]):
                    print(str(self.adjList[i].get(j)) + " ", end="")
                    j += 1
                print()
            i += 1

    def DFSRecursion(self, startVertex):
        self.dfs(startVertex, self.visited)

    def dfs(self, start: int, visited: list):
        visited[int(start)] = True
        print(str(start) + " ", end="")
        visited[int(start)] = True
        i = 0
        while i < len(self.adjList[int(start)]):
            destination = self.adjList[int(start)][i]
            if not visited[destination]:
                self.dfs(destination, visited)
            i += 1

    def main(self, args):

        vertices = 13
        graph = Graph(vertices)
        print("Enter pairs : ")
        while True:
            pair = input()
            if pair == "stop":
                break
            splitted = pair.split(" ")
            edgeFrom = int(splitted[0])
            edgeTo = int(splitted[1])
            graph.addEgde(edgeFrom, edgeTo)
        print("Enter source vertex :")
        source = input()
        print("Preorder: ", end="")
        graph.DFSRecursion(source)

        while True:
            count = 0
            i = 0
            while i < len(self.visited):
                if self.visited[i] == True:
                    count += 1
                i += 1
            if count == vertices:
                break
            else:
                i = 0
                while i < len(self.visited):
                    if self.visited[i] == False:
                        graph.DFSRecursion(i)
                    i += 1


Graph(13).main([])
