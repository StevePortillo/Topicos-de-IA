import random
import matplotlib.pyplot as plt
import networkx as nx
from deap import base, creator, tools, algorithms


distancias_nombres = {
    ("Bilbao", "Celta"): 378, ("Bilbao", "Zaragoza"): 324,
    ("Celta", "Vigo"): 171, ("Celta", "Valladolid"): 235,
    ("Vigo", "Valladolid"): 356, ("Vigo", "Sevilla"): 245,
    ("Valladolid", "Madrid"): 193, ("Valladolid", "Zaragoza"): 390,
    ("Valladolid", "Jaen"): 411,
    ("Zaragoza", "Madrid"): 190, ("Zaragoza", "Albacete"): 215,
    ("Zaragoza", "Barcelona"): 296, ("Zaragoza", "Gerona"): 289,
    ("Madrid", "Albacete"): 251,
    ("Albacete", "Valencia"): 191, ("Albacete", "Granada"): 244,
    ("Albacete", "Murcia"): 150,
    ("Murcia", "Granada"): 257, ("Murcia", "Valencia"): 241,
    ("Barcelona", "Gerona"): 100, ("Barcelona", "Valencia"): 349,
    ("Granada", "Jaen"): 207, ("Granada", "Sevilla"): 211,
    ("Jaen", "Sevilla"): 125,
}


ciudades = list(set(sum(([a, b] for a, b in distancias_nombres.keys()), [])))
indice_a_ciudad = dict(enumerate(ciudades))
ciudad_a_indice = {nombre: i for i, nombre in indice_a_ciudad.items()}


distancias = {}
for (a, b), d in distancias_nombres.items():
    ia, ib = ciudad_a_indice[a], ciudad_a_indice[b]
    distancias[(ia, ib)] = d


def distancia_total(ruta):
    total = 0
    for i in range(len(ruta)):
        a, b = ruta[i], ruta[(i + 1) % len(ruta)]
        if (a, b) in distancias:
            total += distancias[(a, b)]
        elif (b, a) in distancias:
            total += distancias[(b, a)]
        else:
            total += float('inf')
    return total


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(len(ciudades)), len(ciudades))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", lambda ind: (distancia_total(ind),))
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)


def graficar_ruta(indice_ruta):
    ruta = [indice_a_ciudad[i] for i in indice_ruta]
    G = nx.Graph()
    for (a, b), d in distancias_nombres.items():
        G.add_edge(a, b, weight=d)
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(a, b): d for (a, b), d in distancias_nombres.items()})

    ruta_edges = [(ruta[i], ruta[(i + 1) % len(ruta)]) for i in range(len(ruta))]
    ruta_edges_fixed = []
    for a, b in ruta_edges:
        if G.has_edge(a, b):
            ruta_edges_fixed.append((a, b))
        elif G.has_edge(b, a):
            ruta_edges_fixed.append((b, a))

    nx.draw_networkx_edges(G, pos, edgelist=ruta_edges_fixed, edge_color='red', width=3)
    plt.title("Ruta Óptima del Agente Viajero")
    plt.tight_layout()
    plt.show()

def main():
    random.seed(42)
    poblacion = toolbox.population(n=200)
    generaciones = 400
    cxpb = 0.9
    mutpb = 0.2

    algorithms.eaSimple(poblacion, toolbox, cxpb, mutpb, generaciones, verbose=True)
    mejor = tools.selBest(poblacion, k=1)[0]

    mejor_nombres = [indice_a_ciudad[i] for i in mejor]
    print("\nRuta óptima encontrada:")
    print(" → ".join(mejor_nombres))
    print("Distancia total:", distancia_total(mejor))

    graficar_ruta(mejor)

if __name__ == "__main__":
    main()