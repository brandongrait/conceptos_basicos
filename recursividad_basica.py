def suma_recursiva(lista):
    # 1. Caso Base: Si la lista no tiene elementos, la suma es 0
    if not lista: 
        return 0
    
    # 2. Caso Recursivo:
    # lista[0] es el primer elemento
    # lista[1:] es "el resto de la lista" (un recorte)
    print(f"Sumando {lista[0]} y pidiendo el resto de {lista[1:]}")
    
    return lista[0] + suma_recursiva(lista[1:])

# Probemos la función
numeros = [1, 2, 3, 4]
resultado = suma_recursiva(numeros)
print(f"\nEl resultado total es: {resultado}")