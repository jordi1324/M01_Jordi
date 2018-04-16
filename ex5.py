print("CONTADOR DE PARES E IMPARES")
valores = int(input("¿Cuántos valores va a introducir? "))
if valores < 1:
    print("¡Imposible!")
else:
    pares = 0
    for i in range(1, valores+1):
        numero = int(input(f"Escriba el valor {i}: "))
        if numero % 2 ==0:
            pares += 1
    print(f"Ha escrito {pares} números pares y {valores - pares} números impares")
    print("Gracias por su colaboración")