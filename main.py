import random
from tkinter import ttk
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    def __init__(self, n):
        self.m = n
        self.v_dk = [[-1 for _ in range(self.m)]for _ in range(self.m)]

    def add_aresta(self, u, v, d):
        self.v_dk[u][v] = d
        self.v_dk[v][u] = d


MAX = 10**9


def dijkstra(grafo, source, destination):
    distances = [MAX] * grafo.m
    visited = [False] * grafo.m

    distances[source] = 0

    for _ in range(grafo.m):
        min_dist = MAX
        min_vertex = None
        for i in range(grafo.m):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_vertex = i

        if min_vertex is None:
            break

        visited[min_vertex] = True

        for i in range(grafo.m):
            if grafo.v_dk[min_vertex][i] > 0:
                new_dist = distances[min_vertex] + grafo.v_dk[min_vertex][i]
                if new_dist < distances[i]:
                    distances[i] = new_dist

    if distances[destination] == MAX:
        return -1, []
    else:
        path = []
        curr = destination
        while curr != source:
            path.append(curr)
            for i in range(grafo.m):
                if grafo.v_dk[i][curr] > 0 and distances[curr] == distances[i] + grafo.v_dk[i][curr]:
                    curr = i
                    break
        path.append(source)
        return distances[destination], path[::-1]


def main_dijkstra(num_nodes, node_saida, node_chegada, pesos_aleatorios):
    G = nx.DiGraph()
    nodes = []

    print("Inicialização do grafo")
    grafo = Grafo(num_nodes)
    print("Inicialização finalizada")

    print("Leitura do grafo")

    with open('C:/Users/pedro/Documents/projeto algoritmos/Email-EuAll.txt') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                aux = line.split('\t')
                u, v = int(aux[0]), int(aux[1])
                if u not in nodes and u < num_nodes:
                    G.add_node(u)
                    nodes.append(u)
                if u < num_nodes and v < num_nodes:
                    if pesos_aleatorios:
                        grafo.add_aresta(u, v, random.randint(1, 10))
                    else:
                        grafo.add_aresta(u, v, 1)
                    G.add_edge(u, v)
    print("Leitura finalizada")

    print("Dijkstra iniciado")

    distancia = dijkstra(grafo, node_saida, node_chegada)
    print(distancia)

    print("Dijkstra finalizado")

    melhor_caminho = distancia[1]

    pos = nx.spring_layout(G, k=1.5, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=500,
                           node_color='white', edgecolors='black')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='lightblue')
    nx.draw_networkx_edges(G, pos, edgelist=[(melhor_caminho[i], melhor_caminho[i+1])
                           for i in range(len(melhor_caminho)-1)], edge_color='green', width=3)

    plt.axis('off')
    plt.show()

    return distancia

def executar_algoritmo(num_nodes, node_saida, node_chegada, pesos_aleatorios):
    print("Executando algoritmo...")
    res = main_dijkstra(int(num_nodes), int(node_saida),
                        int(node_chegada), pesos_aleatorios)

    resultado = ""

    if res[0] == -1:
        resultado += "Não existe caminho entre os nodes!\n"
    else:
        resultado += "Peso total: " + str(res[0]) + "\nCaminho: ["
        nodes = res[1]
        for i in range(len(nodes)):
            if i < len(nodes) - 1:
                resultado += str(nodes[i]) + ", "
            else:
                resultado += str(nodes[i]) + "]\n"
    return resultado