import random
import time
import math

class RecocidoSimuladoReinas:
    
    def __init__(self, n, temperatura_inicial, factor_enfriamiento, max_iteraciones, solucion_inicial):
        self.n = n  
        self.temperatura = temperatura_inicial  
        self.factor_enfriamiento = factor_enfriamiento  
        self.max_iteraciones = max_iteraciones  
        self.mejor_solucion = solucion_inicial  
        self.mejor_costo = self.calcular_costo(solucion_inicial)  
        self.movimientos = 0  

    def calcular_costo(self, solucion):
        
        ataques = 0
        filas = set()
        diag1 = set()
        diag2 = set()
        
        for col, fila in enumerate(solucion):
            if fila in filas or (fila - col) in diag1 or (fila + col) in diag2:
                ataques += 1
            filas.add(fila)
            diag1.add(fila - col)
            diag2.add(fila + col)

        return ataques

    def generar_vecino(self, solucion):
        
        vecino = solucion[:]
        i, j = random.sample(range(self.n), 2)  
        vecino[i], vecino[j] = vecino[j], vecino[i]  
        return vecino

    def buscar_solucion(self):
        
        inicio_tiempo = time.time()  
        solucion_actual = self.mejor_solucion[:]
        costo_actual = self.mejor_costo

        print("\n--- Inicio de la búsqueda ---")
        print(f"Solución inicial: {solucion_actual}, Coste: {costo_actual}")

        iteracion = 0
        while self.mejor_costo > 0:  
            iteracion += 1
            vecino = self.generar_vecino(solucion_actual)
            costo_vecino = self.calcular_costo(vecino)

            diferencia_costo = costo_vecino - costo_actual

          
            if diferencia_costo < 0 or random.random() < math.exp(-diferencia_costo / self.temperatura):
                solucion_actual = vecino
                costo_actual = costo_vecino

            
            if costo_actual < self.mejor_costo:
                self.mejor_solucion = solucion_actual[:]
                self.mejor_costo = costo_actual

            
            self.temperatura *= self.factor_enfriamiento

           
            print(f"\nIteración {iteracion}")
            print(f"Solución actual: {solucion_actual}")
            print(f"Conflictos actuales: {costo_actual}")
            print(f"Mejor solución encontrada: {self.mejor_solucion}")
            print(f"Mejor costo: {self.mejor_costo}")
            print(f"Temperatura actual: {self.temperatura:.4f}")

            self.movimientos += 1  

        fin_tiempo = time.time()
        tiempo_ejecucion = fin_tiempo - inicio_tiempo

        print("\n--- Métricas ---")
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
        print(f"Número de movimientos: {self.movimientos}")

        return self.mejor_solucion, self.mejor_costo


def solicitar_parametros():
    
    n = 8  
    print("\nAlgoritmo de Recocido Simulado para el problema de las 8 reinas:")
    temperatura_inicial = float(input("Ingrese la temperatura inicial (ej. 1000): "))
    factor_enfriamiento = float(input("Ingrese el factor de enfriamiento (ej. 0.95): "))
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones (ej. 1000): "))

    
    solucion_inicial = list(map(int, input("Ingrese la solución inicial (8 números separados por espacios): ").split()))

    print(f"\nSolución inicial ingresada: {solucion_inicial}")
    return n, temperatura_inicial, factor_enfriamiento, max_iteraciones, solucion_inicial


def imprimir_tablero(solucion):
    
    n = len(solucion)
    print("\nTablero de ajedrez con la solución óptima:")
    for fila in range(n):
        linea = ""
        for columna in range(n):
            if solucion[columna] == fila:
                linea += "Q "
            else:
                linea += ". "
        print(linea)


n, temperatura_inicial, factor_enfriamiento, max_iteraciones, solucion_inicial = solicitar_parametros()

recocido_simulado = RecocidoSimuladoReinas(n, temperatura_inicial, factor_enfriamiento, max_iteraciones, solucion_inicial)
mejor_solucion, mejor_costo = recocido_simulado.buscar_solucion()

print("\nMejor solución encontrada:", mejor_solucion)
print("Número de colisiones:", mejor_costo)

imprimir_tablero(mejor_solucion)