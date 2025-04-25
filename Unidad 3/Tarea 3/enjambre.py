import random
import math
import matplotlib.pyplot as plt

# Datos globales
ciudades = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
num_particulas = 10
iteraciones = 30

def calcular_distancia(ruta):
    return sum(math.sqrt((ciudades[ruta[i]][0]-ciudades[ruta[(i+1)%len(ruta)]][0])**2 + 
               (ciudades[ruta[i]][1]-ciudades[ruta[(i+1)%len(ruta)]][1])**2) 
               for i in range(len(ruta)))

def crear_particula():
    ruta = list(range(len(ciudades)))
    random.shuffle(ruta)
    return {
        'ruta': ruta,
        'distancia': calcular_distancia(ruta),
        'mejor_ruta': ruta.copy(),
        'mejor_distancia': calcular_distancia(ruta)
    }

def mover_particula(particula):
    i, j = random.sample(range(len(particula['ruta'])), 2)
    particula['ruta'][i], particula['ruta'][j] = particula['ruta'][j], particula['ruta'][i]
    particula['distancia'] = calcular_distancia(particula['ruta'])

def evaluar_particula(particula):
    if particula['distancia'] < particula['mejor_distancia']:
        particula['mejor_ruta'] = particula['ruta'].copy()
        particula['mejor_distancia'] = particula['distancia']

def crear_enjambre():
    return [crear_particula() for _ in range(num_particulas)]

def mover_enjambre(enjambre):
    for p in enjambre:
        mover_particula(p)

def evaluar_enjambre(enjambre):
    mejor_global = min(enjambre, key=lambda p: p['distancia'])
    for p in enjambre:
        evaluar_particula(p)
        if p['distancia'] < mejor_global['distancia']:
            mejor_global = p
    return mejor_global

def graficar_ruta(ruta):
    x = [ciudades[i][0] for i in ruta] + [ciudades[ruta[0]][0]]
    y = [ciudades[i][1] for i in ruta] + [ciudades[ruta[0]][1]]
    
    plt.figure(figsize=(6,6))
    plt.plot(x, y, 'b-o')
    for i, (x_pos, y_pos) in enumerate(ciudades):
        plt.text(x_pos, y_pos, str(i), fontsize=12)
    plt.title(f"Distancia: {calcular_distancia(ruta):.2f}")
    plt.grid(True)
    plt.show()

# Ejecución principal
enjambre = crear_enjambre()
mejor_global = min(enjambre, key=lambda p: p['distancia'])

for i in range(iteraciones):
    mover_enjambre(enjambre)
    mejor_actual = evaluar_enjambre(enjambre)
    
    if mejor_actual['distancia'] < mejor_global['distancia']:
        mejor_global = mejor_actual
    
    print(f"Iter {i+1}: Mejor distancia = {mejor_global['distancia']:.2f}")

print("\nMejor ruta encontrada:", mejor_global['ruta'])
graficar_ruta(mejor_global['ruta'])
