Projeto: Implementação do Algoritmo de Dijkstra com Interface Gráfica em Tkinter
Descrição do Projeto
Este projeto implementa o algoritmo de Dijkstra para encontrar o caminho mais curto em um grafo utilizando uma interface gráfica com Tkinter. A base de dados utilizada é a "Email network of a large European Research Institution", que consiste em uma rede de e-mails entre pessoas em uma instituição de pesquisa na Europa. A rede é direcionada, mas para a implementação do algoritmo, considera-se o grafo não direcionado.

Base de Dados
Nome: Email network of a large European Research Institution
Descrição: Rede de e-mails trocados entre membros de uma instituição de pesquisa europeia entre outubro de 2003 e março de 2005.
Nós: 265.214
Arestas: 420.045
Tipo: Direcionado (considerado não direcionado na implementação)
Peso: Não contém peso por padrão, duas opções implementadas:
Peso fixo de 1 para todas as arestas.
Peso aleatório de 1 a 10 para cada aresta.
Funcionalidades
Classe Grafo: Representa o grafo utilizando uma matriz de adjacência.
Algoritmo de Dijkstra: Calcula o caminho mais curto entre dois nós.
Interface Gráfica com Tkinter: Permite a configuração e execução do algoritmo de Dijkstra de forma interativa.
Visualização com Matplotlib e NetworkX: Exibe o grafo e o caminho mais curto encontrado.
