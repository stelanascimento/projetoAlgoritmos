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