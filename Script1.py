import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx*dx + dy*dy)

def coordenadas(nombre):
    while True:
        try:
            entrada = input(f"Introduce {nombre} como 'x y' (ej: 12.5 -3.2): ").strip()
            x_str, y_str = entrada.split()
            return float(x_str), float(y_str)
        except ValueError:
            print("Entrada inválida. Asegúrate de escribir dos números separados por espacio.")

def main():
    print("Cálculo de distancia entre dos coordenadas (2D)")
    x1, y1 = coordenadas("la primera coordenada (x1 y1)")
    x2, y2 = coordenadas("la segunda coordenada (x2 y2)")
    d = distance(x1, y1, x2, y2)
    print(f"Distancia entre ({x1}, {y1}) y ({x2}, {y2}) = {d:.6f}")

if __name__ == "__main__":
    main()
