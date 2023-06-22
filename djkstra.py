import numpy as np
from queue import PriorityQueue
from itertools import product
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(adj_matrix, node_names, begin_node_index=0):
    """
    Encuentra la ruta más corta utilizando el algoritmo de Dijkstra.

    Args:
        adj_matrix (list): 
            Matriz de adyacencia del grafo.
        node_names (list): 
            Lista de nombres de nodos.
        begin_node_index (int, optional): 
            Índice del nodo inicial. Por defecto es 0.

    Returns:
        tuple: 
            Tupla que contiene el peso total del camino más corto y
            la lista de aristas en el camino.
    """
    queue = PriorityQueue()
    current_node = begin_node_index
    covered_nodes = [node_names[current_node]]
    shortest_path = []
    path_weight = 0

    while len(covered_nodes) != len(node_names):

        for name_index, weight in enumerate(adj_matrix[current_node]):

            if weight != 0:
                edge_end = node_names[name_index]
                edge_start = node_names[current_node]

                queue.put((
                    weight,
                    edge_end,
                    edge_start + edge_end
                ))

        for weight, node, edge in iter(queue.get, None):

            if node not in covered_nodes:
                covered_nodes.append(node)
                shortest_path.append(edge)
                current_node = node_names.index(node)
                path_weight += weight
                break

    return path_weight, shortest_path


def show_graph_with_labels(adj_matrix, node_names):
    """
    Muestra un grafo con etiquetas y pesos entre los nodos.

    Args:
        adj_matrix (list): 
            lista de nombres de los nodos del grafo.
        node_names (list):
            matriz de adyacencia que representa las conexiones entre 
            los nodos.

    """
    G = nx.Graph()

    # Agregar nodos al grafo
    G.add_nodes_from(adj_matrix)

    # Agregar aristas al grafo
    for i in range(len(adj_matrix)):
        for j in range(i+1, len(adj_matrix)):
            if node_names[i][j] != 0:
                G.add_edge(
                    adj_matrix[i], adj_matrix[j],
                    weight=node_names[i][j]
                )

    # Mostrar el grafo
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.savefig('graph.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F"]

    adj = [
        [0,  4,  5,  0,  0,  0],  # A
        [4,  0, 11,  9,  7,  0],  # B
        [5, 11,  0,  0,  3,  0],  # C
        [0,  9,  0,  0, 13,  2],  # D
        [0,  7,  3, 13,  0,  6],  # E
        [0,  0,  0,  2,  6,  0],  # F
    ]

    # caminos mas cortos desde cada nodo
    for i in range(0, len(nodes)):
        print(dijkstra(adj, nodes, i))

    # mostrar el grafo
    show_graph_with_labels(nodes, adj)
