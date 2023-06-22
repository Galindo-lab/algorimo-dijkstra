import numpy as np
from queue import PriorityQueue
from itertools import product
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(adj_matrix, node_names, begin_node_index=0):
    """
    Encuentra la ruta más corta utilizando el algoritmo de Dijkstra.

    Args:
        adj_matrix (numpy.ndarray): Matriz de adyacencia del grafo.
        node_names (list): Lista de nombres de nodos.
        begin_node_index (int, optional): Índice del nodo inicial. Por defecto es 0.

    Returns:
        tuple: Tupla que contiene el peso total del camino más corto y la lista de aristas en el camino.
    """
    queue = PriorityQueue()
    current_node = begin_node_index
    covered_nodes = [node_names[current_node]]
    shortest_path = []
    path_weight = 0

    while len(covered_nodes) != len(node_names):
        for enum, weight in enumerate(adj_matrix[current_node]):
            if weight != 0:
                queue.put((weight, node_names[enum], f'{node_names[current_node]}{node_names[enum]}'))

        for weight, node, arist in iter(queue.get, None):
            if node not in covered_nodes:
                covered_nodes.append(node)
                shortest_path.append(arist)
                current_node = node_names.index(node)
                path_weight += weight
                break

    return path_weight, shortest_path



nodes = [
    "A", "B", "C", "D", "E", "F"
]

adj = [
    [0,  4,  5,  0,  0,  0],  # A
    [4,  0, 11,  9,  7,  0],  # B
    [5, 11,  0,  0,  3,  0],  # C
    [0,  9,  0,  0, 13,  2],  # D
    [0,  7,  3, 13,  0,  6],  # E
    [0,  0,  0,  2,  6,  0],  # F
]


for i in range(0, len(nodes)):
    print(dijkstra(adj, nodes, i))