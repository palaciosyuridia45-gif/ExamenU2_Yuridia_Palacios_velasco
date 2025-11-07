# Método del Cuadrado Medio simple
semilla = 1234  # número inicial
n = 5           # cuántos números generar

for i in range(n):
    cuadrado = semilla ** 2
    # Tomamos los 4 dígitos centrales
    semilla = int(str(cuadrado).zfill(8)[2:6])
    print(semilla)
