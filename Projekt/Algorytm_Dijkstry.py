import os
from matplotlib import pyplot as plt
import sys
import networkx as nx
import time

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = sys.maxsize
        self.parent = None
        self.parentEdgeWeight = None

    def add_neighbor(self, neighbor, weight):
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = weight
        else:
            print(neighbor + ' jest już sąsiadem ' + self.name + '!')

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name):
        if name not in self.graph:
            nowyWezel = Node(name)
            self.graph[name] = nowyWezel
        else:
            print('Wierzchołek ' + name + ' już istnieje!')

    def add_edge(self, u, v, w):
        if u in self.graph and v in self.graph:
            self.graph[u].add_neighbor(v, w)
            self.graph[v].add_neighbor(u, w)
        else:
            print('Błąd dodawania krawędzi między ' + u + ' a ' + v +
                  '! Sprawdź, czy obie wierzchołki istnieją w grafie...')

    def Dijkstra(self, s):
        if s not in self.graph:
            print('Wierzchołek o nazwie ' + s + ' nie istnieje w grafie!')
            return

        self.graph[s].distance = 0
        unvisited = MinHeap(self.graph)

        while unvisited.currSize > 0:
            current_node = unvisited.getMin()

            for n, w in current_node.neighbors.items():
                if self.graph[n].distance > current_node.distance + w:
                    self.graph[n].distance = current_node.distance + w
                    self.graph[n].parent = current_node.name
                    self.graph[n].parentEdgeWeight = w
            unvisited.extract()

        for u in self.graph.keys():
            print('Najkrótsza odległość od ' + s + ' do ' + u + ': ' + str(self.graph[u].distance))
        time.sleep(2)


# Klasa MinHeap
class MinHeap:
    def __init__(self, graph):
        self.maxSize = len(graph)
        self.currSize = 0

        self.heap = [Node('dummyNode')] * (self.maxSize + 1)
        self.heap[0].distance = -1 * sys.maxsize
        self.min = 1

        for v in graph.values():
            self.insert(v)
        for pos in range(self.currSize // 2, 0, -1):
            self.heapify(pos)

    def getParent(self, elt):
        return elt // 2

    def getLeftChild(self, elt):
        return elt * 2

    def getRightChild(self, elt):
        return (elt * 2) + 1

    def isLeaf(self, elt):
        if elt <= self.currSize and elt >= self.currSize // 2:
            return True
        else:
            return False

    def swap(self, elt1, elt2):
        self.heap[elt1], self.heap[elt2] = self.heap[elt2], self.heap[elt1]

    def insert(self, elt):
        if self.currSize == self.maxSize:
            return
        self.currSize += 1
        self.heap[self.currSize] = elt

        currElt = self.currSize

        while self.heap[self.getParent(self.currSize)].distance > self.heap[currElt].distance:
            self.swap(self.getParent(self.currSize), currElt)
            currElt = self.getParent(currElt)

    def heapify(self, elt):
        if self.currSize == 0:
            return

        if self.isLeaf(elt):
            return
        if self.heap[elt].distance > self.heap[self.getLeftChild(elt)].distance or \
                self.heap[elt].distance > self.heap[self.getRightChild(elt)].distance:

            smallerChild = self.getLeftChild(elt)
            if self.heap[self.getRightChild(elt)].distance < self.heap[smallerChild].distance:
                smallerChild = self.getRightChild(elt)

            self.swap(elt, smallerChild)
            self.heapify(smallerChild)

    def extract(self):
        self.heap[self.min] = self.heap[self.currSize]
        self.currSize -= 1
        self.heapify(self.min)

    def getMin(self):
        return self.heap[self.min]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_graph_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            g = Graph()

            for line in lines:
                line = line.strip()
                if line.startswith('W:'):
                    _, *node_names = line.split()
                    for node_name in node_names:
                        g.add_node(node_name)
                elif line.startswith('K:'):
                    _, from_node, to_node, weight = line.split()
                    g.add_edge(from_node, to_node, float(weight))

            return g
    except FileNotFoundError:
        print('Plik nie znaleziony!')
        return None

def main():
    g = None

    while True:
        clear_console()
        print('*********************************************')
        print('a: wczytaj graf z pliku')
        print('b: zobacz aktualny stan grafu')
        print('c: uruchom algorytm Dijkstry')
        print('d: wyjdź z programu')
        print('*********************************************')
        action = input('Wybierz akcję: ')
        clear_console()

        if action == 'a':
            file_path = input('Podaj ścieżkę do pliku: ')
            g = load_graph_from_file(file_path)
            if g is not None:
                print('Graf został wczytany z pliku.')
            time.sleep(2)

        elif action == 'b':
            if g is None or len(g.graph) == 0:
                print('Brak wierzchołków w grafie!')
                time.sleep(2)
            else:
                G = nx.Graph()

                for u in g.graph.keys():
                    G.add_node(u)

                for u, v in g.graph.items():
                    for n, w in v.neighbors.items():
                        G.add_edge(u, n, weight=w)

                pos = nx.spring_layout(G)

                nx.draw(G, pos, with_labels=True, node_color='skyblue', font_color='black', font_weight='bold',
                        node_size=700)
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
                plt.draw()
                plt.show()

        elif action == 'c':
            if g is None or len(g.graph) == 0:
                print('Brak wczytanego grafu!')
                time.sleep(2)
            else:
                start = input('Wierzchołek, z którego rozpocząć algorytm Dijkstry: ')
                if start not in g.graph:
                    print('Wierzchołek nie istnieje w grafie...')
                    time.sleep(2)
                else:
                    g.Dijkstra(start)
                    G = nx.Graph()

                    for u in g.graph.keys():
                        G.add_node(u)

                    for u, v in g.graph.items():
                        if v.parent is not None:
                            G.add_edge(v.parent, u, weight=v.parentEdgeWeight)

                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_color='black', font_weight='bold',
                            node_size=700)
                    labels = nx.get_edge_attributes(G, 'weight')
                    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
                    plt.draw()
                    plt.show()

        elif action == 'd':
            return
        else:
            print('Nieprawidłowa akcja! Spróbuj ponownie!')
            time.sleep(2)

if __name__ == "__main__":
    main()