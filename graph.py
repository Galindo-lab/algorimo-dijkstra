
import matplotlib.pyplot as plt
import networkx as nx

from itertools import product
from prettytable import PrettyTable





def unique_items(elements: list) -> list:
    """
    Lanza un error si hay elementos repetidos
    """
    assert len(elements) == len(set(elements)), "Hay elementos repetidos en la lista"
    return elements





def square_matrix(g: list) -> bool:
    """
    Valida si una matriz es cuadrada
    """
    return len(g) == len(g[0])





def zero_matrix(width: int, height: int) -> list:
    """
    Crea una matriz de ceros
    """
    return [[0.0] * width for i in range(height)]





class Graph():
    """
    Esta clase representa un grafo mediante una matriz de 
    adyacencias

    @param labels los nombres de los nodos
    @param nodes numeros de nodos
    @param adjacency_matrix matri de adyacencia
    """

    
    def __init__(self):
        self.labels = []
        self.nodes = 0
        self.adjacency_matrix = []

        
    def add_node(self, name: str):
        self.labels.append(name)
        self.nodes = len(self.labels)
        self.adjacency_matrix = zero_matrix(self.nodes, self.nodes)

        
    def get_node_position(self, node_name: str) -> int:
        """
        Obtiene el indice numerico del nodo o su fila y columna
        en la matriz de adyacencias

        @param node_name nombre del nodo
        @return indice del nodo
        """
        return self.labels.index(node_name)


    def get_weight(self, origin_node: str, destination_node: str) -> float:
        """
        Obtener el peso entre dos nodos, el valor de origen y 
        de destino ya que los grafos no son dirigidos
        
        @param origin_node 
        @param destination_node
        @return weight
        """
        assert origin_node != destination_node, "Un nodo no puede estar unido a si mismo"

        position_a = self.get_node_position(origin_node)
        position_b = self.get_node_position(destination_node)

        return self.adjacency_matrix[position_a][position_b]

    
    def set_weight(self, origin_node: str, destination_node: str, weight: float):
        """
        Obtener el peso entre dos nodos, el valor de origen y 
        de destino ya que los grafos no son dirigidos
        
        @param origin_node 
        @param destination_node
        @return weight
        """

        assert origin_node != destination_node, "Un nodo no puede estar unido a si mismo"

        position_a = self.get_node_position(origin_node)
        position_b = self.get_node_position(destination_node)

        self.adjacency_matrix[position_a][position_b] = weight
        self.adjacency_matrix[position_b][position_a] = weight


    def show_adjacency_matrix(self):
        """
        Imprime el valor de la matriz de adyacencias 
        """
        p = PrettyTable()
        for row in self.adjacency_matrix:
            p.add_row(row)
            
        print(p.get_string(header=False, border=False))
        
    def show_graph(self):
        """
        Imprime el valor de la matriz y muestra una representacion 
        mediante networkx
        """
        
        G = nx.DiGraph()

        size = self.nodes
        for i, j in product(range(size), range(size)):
            if i != j and self.adjacency_matrix[i][j] != 0:
                # argegar nodos al grafo
                G.add_edge(self.labels[i], self.labels[j], weight=self.adjacency_matrix[i][j])
                
        pos = nx.spring_layout(G, seed=1)            # posiciones de los nodos
        labels = nx.get_edge_attributes(G, 'weight') # obtiene los pesos
            
        nx.draw_networkx(G, pos, with_labels=True) # dibuja los nodos 
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # dibuja los pesos
        plt.show()

    @classmethod
    def from_matrix(cls, labels: list, adjacency_matrix: list):
        """
        Crea un objeto de tipo Graph con la tabla de adyacencias 

        @param label lista con los nombres de los nodos
        @param adjacency_matrix matriz de adyacencia del grafo
        @return Graph
        """

        assert square_matrix(adjacency_matrix), "La matriz ingresada no es cuadrada"
        assert len(unique_items(labels)) == len(adjacency_matrix), "El numero de columnas no coincide con la cantidad de etiquetas"

        matrix_size = len(adjacency_matrix)
        for i, j in product(range(matrix_size), range(matrix_size)):
            assert adjacency_matrix[i][i] == 0, f"El nodo de la fila {i} esta conectado con si mismo"
            assert adjacency_matrix[i][j] == adjacency_matrix[j][i], f"El Nodo [{i},{j}] no es simetrico con [{j},{i}]"

        foo = Graph(labels)
        foo.adjacency_matrix = adjacency_matrix
        return foo
