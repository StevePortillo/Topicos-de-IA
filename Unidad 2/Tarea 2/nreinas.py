#Portillo Zuñiga Steve Javier

import random
import time

class BusquedaTabuNReinas:
    def __init__(self, n, tenencia_tabu, max_iteraciones, tamano_vecindario):
        self.n = n 
        self.tenencia_tabu = tenencia_tabu  
        self.max_iteraciones = max_iteraciones  
        self.tamano_vecindario = tamano_vecindario  
        self.lista_tabu = [] 
        self.mejor_solucion = None  
        self.mejor_costo = float('inf')  
        self.movimientos = 0  

    def solucion_inicial(self):
        # Genera una solución inicial aleatoria
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def costo(self, solucion):
        # Calcula el número de conflictos (reinas que se atacan)
        conflictos = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                    conflictos += 1
        return conflictos

    def generar_vecindario(self, solucion):
        # Genera un vecindario de soluciones
        vecindario = []
        for _ in range(self.tamano_vecindario):
            vecino = solucion.copy()
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.n - 1)
            vecino[i] = j
            vecindario.append(vecino)
        return vecindario

    def busqueda_tabu(self):
        # Inicialización
        tiempo_inicio = time.time()  # Iniciar el contador de tiempo
        solucion_actual = self.solucion_inicial()
        costo_actual = self.costo(solucion_actual)
        self.mejor_solucion = solucion_actual
        self.mejor_costo = costo_actual

        print("Iteración 0 - Solución inicial:", solucion_actual, "Conflictos:", costo_actual)
        print("Lista Tabú:", self.lista_tabu)

        # Bucle principal
        for iteracion in range(1, self.max_iteraciones + 1):
            vecindario = self.generar_vecindario(solucion_actual)
            mejor_vecino = None
            mejor_costo_vecino = float('inf')

            # Evaluar vecindario
            for vecino in vecindario:
                costo_vecino = self.costo(vecino)
                if costo_vecino < mejor_costo_vecino and vecino not in self.lista_tabu:
                    mejor_vecino = vecino
                    mejor_costo_vecino = costo_vecino

            # Actualizar la mejor solución
            if mejor_costo_vecino < self.mejor_costo:
                self.mejor_solucion = mejor_vecino
                self.mejor_costo = mejor_costo_vecino

            # Actualizar la lista Tabú
            self.lista_tabu.append(mejor_vecino)
            if len(self.lista_tabu) > self.tenencia_tabu:
                self.lista_tabu.pop(0)

            # Actualizar la solución actual
            solucion_actual = mejor_vecino
            costo_actual = mejor_costo_vecino
            self.movimientos += 1  # Incrementar el contador de movimientos

            # Mostrar información de la iteración
            print(f"\nIteración {iteracion}")
            print("Solución actual:", solucion_actual)
            print("Conflictos actuales:", costo_actual)
            print("Mejor solución encontrada:", self.mejor_solucion)
            print("Mejor costo (conflictos):", self.mejor_costo)
            print("Lista Tabú:", self.lista_tabu)

            # Si se encuentra una solución óptima, terminar
            if self.mejor_costo == 0:
                print("\n¡Solución óptima encontrada!")
                break

        # Calcular el tiempo de ejecución
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio

        # Mostrar métricas
        print("\n--- Métricas ---")
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
        print(f"Número de movimientos: {self.movimientos}")

        return self.mejor_solucion, self.mejor_costo

# Parámetros del algoritmo
n = 8  
tenencia_tabu = 5 
max_iteraciones = 100 
tamano_vecindario = 8  

# Ejecutar el algoritmo
bt = BusquedaTabuNReinas(n, tenencia_tabu, max_iteraciones, tamano_vecindario)
mejor_solucion, mejor_costo = bt.busqueda_tabu()

# Mostrar resultados finales
print("\nMejor solución encontrada:", mejor_solucion)
print("Número de conflictos:", mejor_costo)

# Visualizar el tablero
def imprimir_tablero(solucion):
    for fila in range(n):
        linea = ""
        for columna in range(n):
            if solucion[columna] == fila:
                linea += "Q "
            else:
                linea += ". "
        print(linea)

print("\nTablero de ajedrez con las reinas colocadas:")
imprimir_tablero(mejor_solucion)