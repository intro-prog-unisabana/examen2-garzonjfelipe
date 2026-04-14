# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


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
        s = sum(times[i:i + k])
        if s < best:
            best = s
    return best

def longest_decreasing_streak(timer):
    times = timer["times"]
    if not times:
        return 0
    best = current = 1
    for i in range(1, len(times)):
        if times[i] < times[i - 1]:
            current += 1
            if current > best:
                best = current
        else:
            current = 1
    return best

def main():
    timer = init(10)
    for t in [1.85, 1.02, 0.91, 0.87, 0.85, 0.82, 0.82, 0.82, 0.83, 0.90]:
        timer = add_lap(timer, t)
    print("numero de vueltas =", count(timer))
    print("tiempo acumulado =", cumulative_time(timer))
    print("vuelta mas rapida =", fastest_lap(timer))
    print("50m mas rapidos =", fastest_multi_lap(timer, 5))
    print("racha mas larga =", longest_decreasing_streak(timer))
    print(format_laps(timer))

if __name__ == "__main__":
    main()




    # TODO: Pedir el nombre del archivo al usuario usando input()
    
    # TODO: Abrir el archivo y leer el numero de vueltas n
    
    # TODO: Crear el cronometro usando lap_timer.init(n)
    
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    
   



