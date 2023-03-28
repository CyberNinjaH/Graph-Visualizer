from pyvis.network import Network
import os
import random
from bs4 import BeautifulSoup
net = Network(notebook=True, directed=False, height='500px', width='100%',
                  bgcolor='white', font_color="black")
fileNodes = open("file.txt", "r")
contentNodes = fileNodes.readlines()
fileColors = open("colors.txt", "r")
contentColors = fileColors.readlines()
colors = []
web_path = "graph.html"

edges = set()
nodes = set()

def GetColor():
    return colors[random.randint(0, 1)]

def AddToGraph():
    for i in nodes:
        color = GetColor()
        net.add_node(i, label=str(i), color=color)

    for i in edges:
        a = i[0]
        b = i[1]
        net.add_edge(a, b)

def GetFromFiles():
    n_nodes = int(contentNodes[0]) + 1
    del contentNodes[0]

    for line in range(0, n_nodes - 1):
        node = contentNodes[line].split("\n")
        nodes.add(int(node[0]))

    print(nodes)

    del contentNodes[0:n_nodes - 1]
    del contentNodes[0]
    

    for line in contentNodes:
        num = line.split(" ")
        a = int(num[0])
        b = int(num[1])

        pair = (a, b)
        edges.add(pair)
    for line in contentColors:
        colors.append(line)

GetFromFiles()
AddToGraph()

net.show(web_path)