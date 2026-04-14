# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
  def init(max_laps):
    return {"max": max_laps, "times": [], "total": 0.0}

def add_lap(timer, time):
    timer["times"].append(time)
    timer["total"] += time
    return timer

def count(timer):
    return len(timer["times"])

def cumulative_time(timer):
    return timer["total"]

def format_laps(timer):
    return str(timer["times"])

def fastest_lap(timer):
    return min(timer["times"])

def fastest_multi_lap(timer, k):
    times = timer["times"]
    best = sum(times[:k])
    for i in range(1, len(times) - k + 1):
        current = sum(times[i:i+k])
        if current < best:
            best = current
    return best




    # TODO: Pedir el nombre del archivo al usuario usando input()
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    
    # TODO: Crear el cronometro usando lap_timer.init(n)
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    
    pass


if __name__ == "__main__":
    main()
