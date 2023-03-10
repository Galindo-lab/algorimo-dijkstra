from itertools import product
from graph import Graph
from dijkstra import find


def captura_nombre_nodos(grafo):
  n_labels = int(input("Numero de nodos en el grafo: "))

  print("\nCrear los nodos del grafo")

  while n_labels > 0:
    label = input("Nombre del nodo: ")

    if label in grafo.labels:
      print(f"El nodo {label} ya existe en el grafo")
      continue

    print(f"Nodo {label} agregado al grafo!")
    grafo.add_node(label)
    n_labels -= 1


def ajustar_pesos_nodos(grafo):
  print("\nCapturar los pesos entre nodos")

  for i, j in product(grafo.labels, grafo.labels):
    if i == j:
      # si es el mismo nodo
      continue

    if grafo.get_weight(i, j) != 0:
      # si el nodo ya esta definido
      continue

    foo = input(f"Peso entre {i} y {j}: ")
    if foo == "":
      weight = 0
    else:
      weight = float(foo)

    grafo.set_weight(i, j, weight)

  print("")


def corregir_peso(grafo):
  a = input("Nombre del nodo origen: ")
  b = input("Nombre del nodo destino: ")

  if not a in grafo.labels:
    print(f"El nodo {a} no existe\n")
    return

  if not b in grafo.labels:
    print(f"El nodo {b} no existe\n")
    return

  weight = float(input(f"Distancia entre {a} y {b}: "))
  grafo.set_weight(a, b, weight)
  print("")


if __name__ == "__main__":
  grafo = Graph()
  captura_nombre_nodos(grafo)
  ajustar_pesos_nodos(grafo)

  foo = input("nodo de origen (default primero ingresado): ")

  nodo_fuente = grafo.labels.index(foo) if foo in grafo.labels else -1

  while True:
    # mostrar la matriz capturada
    print("Matriz de adyacencias:")
    grafo.show_adjacency_matrix()
    find(grafo.labels, grafo.adjacency_matrix, nodo_fuente)
    grafo.show_graph()

    # correcciones
    #op = input("\nLos pesos son correctas (y/n)? ")
    #if op == "y": break
    #if op == "n": corregir_peso(grafo)

# a = Graph.from_matrix(
#     ['A', 'B', 'C', 'D', 'E'],
#     [  # A  B  C  D  E
#         [0, 6, 0, 1, 0],  # A
#         [6, 0, 5, 2, 2],  # B
#         [0, 5, 0, 0, 5],  # C
#         [1, 2, 0, 0, 1],  # D
#         [0, 2, 5, 1, 0],  # E
#     ])

# a = Graph.from_matrix(
#     [ 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'J'],
#     [# A  B  C  D  F  G  H  J
#       [0, 4, 2, 0, 0, 7, 0, 0],  # A - 0
#       [4, 0, 0, 2, 0, 0, 0, 0],  # B - 1
#       [2, 0, 0, 0, 8, 3, 0, 0],  # C - 2
#       [0, 2, 0, 0, 0, 5, 6, 0],  # D - 3
#       [0, 0, 8, 0, 0, 0, 0, 3],  # F - 4
#       [7, 0, 3, 5, 0, 0, 0, 4],  # G - 5
#       [0, 0, 0, 6, 0, 0, 0, 2],  # H - 6
#       [0, 0, 0, 0, 3, 4, 2, 0],  # J - 7
#     ]
# )

# a.show_graph()

# # show_graph_with_labels(a.adjacency_matrix, a.labels)
