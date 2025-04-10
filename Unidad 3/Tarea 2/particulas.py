import random
import matplotlib.pyplot as plt


POS_MIN, POS_MAX = -10, 10
VEL_MIN, VEL_MAX = -2, 2
NUM_PARTICULAS = 10


def funcion_objetivo(x, y):
    return -(x**2 + y**2)


particulas = []

for _ in range(NUM_PARTICULAS):
    x = random.uniform(POS_MIN, POS_MAX)
    y = random.uniform(POS_MIN, POS_MAX)
    vx = random.uniform(VEL_MIN, VEL_MAX)
    vy = random.uniform(VEL_MIN, VEL_MAX)
    valor = funcion_objetivo(x, y)

    particula = {
        "posicion": {"x": x, "y": y},
        "velocidad": {"x": vx, "y": vy},
        "memoria": {
            "mejor_x": x,
            "mejor_y": y,
            "mejor_valor": valor
        },
        "valor": valor
    }

    particulas.append(particula)


for i, p in enumerate(particulas):
    print(f"Partícula {i+1}: {p}")


plt.figure(figsize=(6, 6))
for p in particulas:
    plt.scatter(p["posicion"]["x"], p["posicion"]["y"], label='Partícula')

plt.xlim(POS_MIN, POS_MAX)
plt.ylim(POS_MIN, POS_MAX)
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title("Visualización de Partículas")
plt.grid(True)
plt.show()
