# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer

def main():
    nombre = input("Nombre del archivo: ")
    with open(nombre, "r") as f:
        lineas = f.read().splitlines()

    n = int(lineas[0])
    timer = lap_timer.init(n)

    for t in lineas[1:]:
        timer = lap_timer.add_lap(timer, float(t))

    print(lap_timer.longest_decreasing_streak(timer))

if __name__ == "__main__":
    main()



    # TODO: Pedir el nombre del archivo al usuario usando input()
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    
    # TODO: Crear el cronometro usando lap_timer.init(n)
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    
   



