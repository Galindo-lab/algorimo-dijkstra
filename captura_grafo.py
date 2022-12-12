# import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from prettytable import PrettyTable





def show_graph_with_labels(adjacency_matrix, mylabels):
    # matriz de adyasencias
    p = PrettyTable()
    for row in adjacency_matrix:
        p.add_row(row)

    print(p.get_string(header=False, border=False))

    # grafo
    G = nx.DiGraph()
    
    size = len(adjacency_matrix)
    for i in range(size):
        for j in range(size):
            if i != j and adjacency_matrix[i][j] != 0:
                G.add_edge(mylabels[i],
                           mylabels[j],
                           weight=adjacency_matrix[i][j])

    pos = nx.spring_layout(G, seed=1)            # posisciones de los nodos
    labels = nx.get_edge_attributes(G, 'weight') # obtiene los pesos
    
    nx.draw_networkx(G, pos, with_labels=True) # dibuja los nodos 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # dibuja los pesos
    plt.show()



    

def unique_items(elements: list) -> list:
    """Lanza un error si hay elementos repetidos"""
    assert len(elements) == len(
        set(elements)), "Hay elementos repetidos en la lista"

    return elements





def square_matrix(g: list) -> bool:
    """Valida si una matriz es cuadrada"""
    return len(g) == len(g[0])





def zero_matrix(width: int, height: int) -> list:
    """Crea una matriz de ceros"""
    mtx = []
    for i in range(width):
        aux = [0] * height
        mtx.append(aux)
    return mtx





class Graph():
    """Esta clase representa un grafo mediante una matriz de 
    adyacensias"""




    

    def __init__(self, labels: list):
        self.labels = unique_items(labels)
        self.nodes = len(self.labels)
        self.adjacency_matrix = zero_matrix(self.nodes, self.nodes)

        
    def get_node_position(self, node_name: str) -> int:
        """Obtiene el indice numerico del nodo"""

        return self.labels.index(node_name)



    def get_weight(self, origin_node: str, destination_node: str):

        assert origin_node != destination_node, "Un nodo no puede estar unido a si mismo"

        position_a = self.get_node_position(origin_node)
        position_b = self.get_node_position(destination_node)

        return self.adjacency_matrix[position_a][position_b]

    
    def set_weight(self, origin_node: str, destination_node: str,
                               weight: float):
        """Cambia el peso de la union de dos nodos"""

        assert origin_node != destination_node, "Un nodo no puede estar unido a si mismo"

        position_a = self.get_node_position(origin_node)
        position_b = self.get_node_position(destination_node)

        self.adjacency_matrix[position_a][position_b] = weight
        self.adjacency_matrix[position_b][position_a] = weight





        
    @classmethod
    def from_matrix(cls, labels: list, adjacency_matrix: list):
        """Carga el grafo desde una matriz"""

        assert square_matrix(
            adjacency_matrix), "La matriz ingresada no es cuadrada"

        foo = len(unique_items(labels))
        assert foo == len(
            adjacency_matrix
        ), "El numero de columnas no coincide con la cantidad de etiquetas"

        for i in range(0, foo):
            for j in range(0, foo):
                assert adjacency_matrix[i][
                    i] == 0, f"El nodo de la fila {i} esta conectado con si mismo"

                assert adjacency_matrix[i][j] == adjacency_matrix[j][
                    i], f"El Nodo [{i},{j}] no es simetrico con [{j},{i}]"

        foo = Graph(labels)
        foo.adjacency_matrix = adjacency_matrix
        return foo



    

if __name__ == "__main__":

    # a = Graph.from_matrix(
    #     ['A', 'B', 'C', 'D', 'E'],
    #     [  #A  B  C  D  E
    #         [0, 6, 0, 1, 0],  # A
    #         [6, 0, 5, 2, 2],  # B
    #         [0, 5, 0, 0, 5],  # C
    #         [1, 2, 0, 0, 1],  # D
    #         [0, 2, 5, 1, 0],  # E
    #     ])

    # a = Graph.from_matrix(
    #     ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'J'],
    #     [  # A  B  C  D  F  G  H  J
    #         [0, 4, 2, 0, 0, 7, 0, 0],  # A - 0
    #         [4, 0, 0, 2, 0, 0, 0, 0],  # B - 1
    #         [2, 0, 0, 0, 8, 3, 0, 0],  # C - 2
    #         [0, 2, 0, 0, 0, 5, 6, 0],  # D - 3
    #         [0, 0, 8, 0, 0, 0, 0, 3],  # F - 4
    #         [7, 0, 3, 5, 0, 0, 0, 4],  # G - 5
    #         [0, 0, 0, 6, 0, 0, 0, 2],  # H - 6
    #         [0, 0, 0, 0, 3, 4, 2, 0],  # J - 7
    #     ]
    # )

    # show_graph_with_labels(a.adjacency_matrix, a.labels)


    labels = []
    n_labels = int(input("Numero de nodos en el grafo: "))
    
    while n_labels > 0:
        print("")
        label = input(f"Nombre del nodo: ")
        
        if not label in labels:
            print(f"Nodo {label} agregado al grafo!")
            labels.append(label)
            n_labels -= 1
            continue

        print(f"El nodo {label} ya existe en el grafo")
        

    grafo = Graph(labels)       # -----------------------------
    
    for i in labels:
        for j in labels:
            
            if i == j: continue # si es el mismo nodo
            if grafo.get_weight(i, j) != 0: continue # si el nodo ya esta definido

            print("")
            weight = float(input(f"Distancia de {i} -> {j}: "))
            grafo.set_weight(i, j, weight)
            
                
    show_graph_with_labels(grafo.adjacency_matrix, grafo.labels)


    op = ''
    while op != 'y':
        op =input("Las distancias son correctas (y/n)?")
        
        if op == "n":
            a = input(f"Nombre del nodo origen: ")
            b = input(f"Nombre del nodo destino: ")

            if not a in labels:
                print(f"El nodo {a} no existe")
                continue

            if not b in labels:
                print(f"El nodo {b} no existe")
                continue

            weight = float(input(f"Distancia de {a} -> {b}: "))
            grafo.set_weight(a, b, weight)
            show_graph_with_labels(grafo.adjacency_matrix, grafo.labels)
